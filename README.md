# 🎓 Student Management System

A modern, full-featured **Student Management System** built with **Python**, **Flask**, **SQLAlchemy**, and **Bootstrap 5**. The application provides secure authentication, role-based access control, analytics dashboards, student management, data export, activity logging, and system configuration.

This project was developed as a portfolio application to demonstrate full-stack web development skills using Flask.

---

# 🚀 Live Demo

**Live Website:**
https://student-management-system-zqsh.onrender.com


---

# 📸 Screenshots

| Page | Screenshot |
|-------|------------|
| Login | `./static/screenshots/login.png` |
| Dashboard | `static/screenshots/Dashboard.png` |
| Students | `static/screenshots/Students.png` |
| Analytics | `static/screenshots/analytics.png` |
| Users | `static/screenshots/users.png` |
| Activity Logs | `static/screenshots/activityLogs.png` |
| Settings | `static/screenshots/settings.png` |
| Profile | `static/screenshots/profile.png` |
| Add students | `static/screenshots/Add_students.png` |


---

# ✨ Features

## Authentication

- Secure Login
- Logout
- Password Hashing
- Flask-Login Authentication
- Session Management

---

## User Management

- Administrator Account
- Staff Account
- Create Users
- Edit Users
- Delete Users
- Prevent Self-Deletion
- Change Password
- User Profiles
- Role-Based Access Control

---

## Student Management

- Add Student
- View Students
- Edit Student
- Delete Student
- Student Profile
- Search Students
- Pagination

---

## Dashboard

- Total Students
- Total Programs
- Average Level
- Students With Email
- Students by Program
- Students by Level
- Recent Students
- Analytics Cards

---

## Charts & Analytics

- Program Distribution
- Student Levels
- Responsive Charts using Chart.js

---

## Export Features

- Export CSV
- Export Excel (.xlsx)
- Export PDF

---

## Activity Logs

- Login History
- Student Created
- Student Updated
- Student Deleted
- Export History
- User Management Logs

---

## System Settings

- School Name
- Administrator Email
- Students Per Page
- Dark / Light Theme
- Logo Upload

---

## UI Features

- Responsive Design
- Bootstrap 5
- Bootstrap Icons
- Custom 404 Page
- Custom 500 Page
- Clean Dashboard
- Professional Admin Layout

---

# 🛠️ Built With

### Backend

- Python
- Flask
- SQLAlchemy
- Flask-Login

### Database

- SQLite

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js

### Reporting

- Pandas
- OpenPyXL
- ReportLab

### Deployment

- Render

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
student-management-system/

│
├── app.py
├── config.py
├── extensions.py
├── models.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
│
├── database/
│   └── database.db
│
├── static/
│   ├── css/
│   ├── js/
│   ├── uploads/
│   └── screenshots/
│
└── templates/
    ├── base.html
    ├── login.html
    ├── index.html
    ├── students.html
    ├── add_student.html
    ├── edit_student.html
    ├── profile.html
    ├── users.html
    ├── settings.html
    ├── logs.html
    ├── analytics.html
    ├── 404.html
    └── 500.html
```

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/fannaremeaboubacarabdougana/student-management-system.git

---

## Navigate to the project

```bash
cd student-management-system
```

---

## Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 🔐 Default Login

## Administrator

Username

```
admin
```

Password

```
admin123
```

# 📈 Skills Demonstrated

- Full Stack Web Development
- Flask
- Authentication
- Authorization
- CRUD Operations
- Database Design
- SQLAlchemy ORM
- Pagination
- Search Functionality
- Dashboard Development
- Data Visualization
- Export Reports
- Activity Logging
- Responsive UI Design
- Deployment
- Git Workflow

---

# 🌍 Deployment

This application is deployed on **Render**.

Deployment includes:

- GitHub Integration
- Automatic Deployments
- Production Environment
- Cloud Hosting

---

# 💡 Future Improvements

- Email Notifications
- Student Attendance Module
- Course Management
- Grade Management
- Parent Portal
- REST API
- React Frontend
- PostgreSQL Database
- Docker Support
- Unit Testing
- CI/CD Pipeline
- Multi-School Support

---

# 👨‍💻 Author

**Fannareme Aboubacar Abdou Gana**

Management Information Systems (MIS) Student

- GitHub: https://github.com/fannaremeaboubacarabdougana/student-management-system.git
- Email: fannaremeaboubacarabdougana@gmail.com

---

# 📄 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project.

---

# ⭐ Acknowledgements

Special thanks to the Flask, Bootstrap, SQLAlchemy, Pandas, OpenPyXL, ReportLab, and Chart.js communities for providing excellent open-source tools that made this project possible.