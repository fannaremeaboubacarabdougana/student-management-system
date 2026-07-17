from flask import Blueprint, render_template
from flask_login import login_required
from models import Student

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/")
@login_required
def home():

    students = Student.query.all()

    total_students = len(students)

    total_programs = len(set(student.program for student in students))

    average_level = round(
        sum(student.level for student in students) / total_students
        if total_students
        else 0
    )

    students_with_email = sum(1 for student in students if student.email)

    return render_template(
        "index.html",
        total_students=total_students,
        total_programs=total_programs,
        average_level=average_level,
        students_with_email=students_with_email,
    )
