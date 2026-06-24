import csv
import datetime
import os
import time

import cv2


def is_same_face(existing_faces, x, y, w, h, overlap_threshold=0.4):
    """Return True when a face rectangle matches a previously saved face."""
    new_area = w * h
    new_right = x + w
    new_bottom = y + h

    for old_x, old_y, old_w, old_h in existing_faces:
        old_right = old_x + old_w
        old_bottom = old_y + old_h
        old_area = old_w * old_h

        intersect_width = max(0, min(new_right, old_right) - max(x, old_x))
        intersect_height = max(0, min(new_bottom, old_bottom) - max(y, old_y))
        intersection_area = intersect_width * intersect_height

        if intersection_area == 0:
            continue

        overlap_ratio = intersection_area / max(new_area, old_area)
        if overlap_ratio >= overlap_threshold:
            return True

    return False


def log_attendance(log_path, face_count):
    file_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as log_file:
        writer = csv.writer(log_file)
        if not file_exists:
            writer.writerow(["timestamp", "faces_detected"])
        writer.writerow([datetime.datetime.now().isoformat(timespec="seconds"), face_count])


def main():
    output_dir = os.path.join(os.path.dirname(__file__), "attendance_records")
    os.makedirs(output_dir, exist_ok=True)

    log_path = os.path.join(output_dir, "attendance_log.csv")
    video_path = os.path.join(output_dir, "attendance_recording.mp4")

    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    if face_cascade.empty():
        raise RuntimeError(f"Unable to load Haar cascade from {cascade_path}")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Unable to open webcam")
        return

    start_time = time.time()
    duration_seconds = 5
    frame_scale = 0.6
    snapshot_count = 0
    detected_faces = []
    video_writer = None

    print("Starting webcam capture for 5 seconds. Press 'q' to exit early.")

    while True:
        elapsed = time.time() - start_time
        if elapsed >= duration_seconds:
            print("5 seconds elapsed; ending capture.")
            break

        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame from webcam")
            break

        if video_writer is None:
            height, width = frame.shape[:2]
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            video_writer = cv2.VideoWriter(video_path, fourcc, 20.0, (width, height))

        video_writer.write(frame)

        small_frame = cv2.resize(frame, None, fx=frame_scale, fy=frame_scale, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _ = cv2.Canny(blurred, 50, 150)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

        if len(faces) == 0:
            cv2.putText(frame, "No faces found", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
        else:
            for i, (x, y, w, h) in enumerate(faces, start=1):
                x1 = int(x / frame_scale)
                y1 = int(y / frame_scale)
                w1 = int(w / frame_scale)
                h1 = int(h / frame_scale)
                cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
                cv2.putText(frame, f"Face {i}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                if not is_same_face(detected_faces, x, y, w, h):
                    detected_faces.append((x, y, w, h))
                    face_image = frame[y1:y1 + h1, x1:x1 + w1]
                    if face_image.size > 0:
                        snapshot_count += 1
                        snapshot_filename = f"attendance_face_{snapshot_count:02d}.jpg"
                        snapshot_path = os.path.join(output_dir, snapshot_filename)
                        cv2.imwrite(snapshot_path, face_image)
                        print(f"Saved attendance snapshot: {snapshot_path}")

            cv2.putText(frame, "Attendance Marked", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        cv2.imshow("Smart Attendance (Original Video)", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Exit requested by user")
            break

    cap.release()
    if video_writer is not None:
        video_writer.release()
    cv2.destroyAllWindows()

    log_attendance(log_path, snapshot_count)
    print(f"Attendance session ended. Video saved to: {video_path}")
    print(f"Attendance log updated: {log_path}")


if __name__ == "__main__":
    main()
