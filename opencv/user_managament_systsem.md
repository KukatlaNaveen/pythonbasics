Employe Before register:

1.Employe should register with name and password
name:string
password :alpanumeric

2.Employe should login with name and password
name:string
password :alpanumeric

------what Employe can do ----
1.after employe login employe should landing the employe page
2.Employe should able to View profile:
3.Employe should View and download offer letter
4.Employe should Accept or reject offer
5.Employe should Upload required documents
6.Employe should Complete onboarding forms
7.Employe should View joining date and reporting manager
8.Employe should Change password
9.Employe should Update personal details
10.Employe should View notifications



2.Permissions:
    Employe should able to click the navbar
    Employe should able to View profile:

1.------Personal Information----

    Employee can view:

            Profile Photo
            Employee ID
            First Name
            Last Name
            Gender
            Date of Birth
            Marital Status
            Blood Group
            Nationality

    Contact Information
            Email
            Phone Number
            Alternate Phone Number
            Address
            Emergency Contact

    Actions:

            employ  should Edit phone number
            employe should Edit address
            employe should Upload profile picture
            employe cannot edit Employee ID
            employe Cannot edit Department
            employe Cannot edit Designation

2. ----Employment Details-----

    Employee can view:

            Employee Code
            Department
            Designation
            Joining Date
            Reporting Manager
            Employment Type
            Work Location

3. -----Documents----

    Employee can:

            View
            Offer Letter
            Appointment Letter
            Salary Slips
            Experience Letter
            Promotion Letters
            Tax Documents
    Actions

        Download PDF
        Upload documents

            Aadhaar Card
            PAN Card
            Passport
            Degree Certificates
            Bank Passbook

4. ----Attendance---

    Employee can:

            Check In
            Check Out
            View Daily Attendance
            View Monthly Attendance
            View Working Hours

5.---Leave Management----

    Employee can:

    Apply Leave

    Types:

            Casual Leave
            Sick Leave
            Paid Leave
            Work From Home
    View
            Leave Balance
            Pending Requests
            Approved Leaves
            Rejected Leaves
    Actions

            Create leave request
            Cancel pending request

6.-----Payroll-----

    Employee can view:

            Salary Structure
            Monthly Salary Slips
            Tax Details
            Bonuses
            Deductions
        
    Actions:
            Download Payslip
            Cannot modify salary






Users Table:    id
                name
                email
                password
                role
                status

Employe Table:  id (PK)
                employee_code
                user_id (FK)
                department_id (FK)
                manager_id (FK -> employees.id)
                first_name
                last_name
                gender
                phone
                dob
                joining_date
                designation
                work_location
                created_at