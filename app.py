from config import Config
from models import db, Student
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import func

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():

    total_students = Student.query.count()

    total_programs = db.session.query(
        func.count(func.distinct(Student.program))
    ).scalar()

    average_level = db.session.query(func.avg(Student.level)).scalar()

    students_with_email = Student.query.filter(Student.email != None).count()

    if average_level is None:
        average_level = 0

    return render_template(
        "index.html",
        total_students=total_students,
        total_programs=total_programs,
        average_level=round(average_level),
        students_with_email=students_with_email,
    )


@app.route("/students")
def students():

    search = request.args.get("search")

    if search:
        students = Student.query.filter(
            (Student.student_id.contains(search))
            | (Student.first_name.contains(search))
            | (Student.last_name.contains(search))
            | (Student.email.contains(search))
            | (Student.program.contains(search))
        ).all()

    else:
        students = Student.query.all()

    return render_template("students.html", students=students, search=search)


@app.route("/students/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":
        student = Student(
            student_id=request.form["student_id"],
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            phone=request.form["phone"],
            program=request.form["program"],
            level=request.form["level"],
        )

        db.session.add(student)
        db.session.commit()

        flash("Student added successfully!", "success")

        return redirect(url_for("students"))

    return render_template("add_student.html")


@app.route("/students/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    student = Student.query.get_or_404(id)

    if request.method == "POST":
        student.student_id = request.form["student_id"]
        student.first_name = request.form["first_name"]
        student.last_name = request.form["last_name"]
        student.email = request.form["email"]
        student.phone = request.form["phone"]
        student.program = request.form["program"]
        student.level = request.form["level"]

        db.session.commit()

        flash("Student updated successfully!", "success")

        return redirect(url_for("students"))

    return render_template("edit_student.html", student=student)


@app.route("/students/delete/<int:id>")
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    flash("Student deleted successfully!", "danger")

    return redirect(url_for("students"))


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
