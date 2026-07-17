from flask import Flask, render_template, request, redirect, url_for, flash

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user,
)
from sqlalchemy import func

from config import Config
from extensions import db, login_manager
from models import Student, User

# Blueprints (we'll enable these later)
# from routes.auth import auth
# from routes.dashboard import dashboard

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Register blueprints (later in Sprint 15)
# app.register_blueprint(auth)
# app.register_blueprint(dashboard)


@app.route("/")
@login_required
def home():

    total_students = Student.query.count()

    total_programs = db.session.query(
        func.count(func.distinct(Student.program))
    ).scalar()

    average_level = db.session.query(func.avg(Student.level)).scalar()

    highest_level = db.session.query(func.max(Student.level)).scalar()

    lowest_level = db.session.query(func.min(Student.level)).scalar()

    students_with_email = Student.query.filter(Student.email != None).count()

    recent_students = Student.query.order_by(Student.id.desc()).limit(5).all()

    program_counts = (
        db.session.query(Student.program, func.count(Student.id))
        .group_by(Student.program)
        .all()
    )

    if average_level is None:
        average_level = 0

    if highest_level is None:
        highest_level = 0

    if lowest_level is None:
        lowest_level = 0

    return render_template(
        "index.html",
        total_students=total_students,
        total_programs=total_programs,
        average_level=round(average_level),
        highest_level=highest_level,
        lowest_level=lowest_level,
        students_with_email=students_with_email,
        recent_students=recent_students,
        program_counts=program_counts,
    )


@app.route("/students")
@login_required
def students():

    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)

    query = Student.query

    if search:
        query = query.filter(
            (Student.student_id.contains(search))
            | (Student.first_name.contains(search))
            | (Student.last_name.contains(search))
            | (Student.email.contains(search))
            | (Student.program.contains(search))
        )

    pagination = query.paginate(
        page=page,
        per_page=5,
        error_out=False,
    )

    return render_template(
        "students.html",
        students=pagination.items,
        pagination=pagination,
        search=search,
    )


@app.route("/students/<int:id>")
@login_required
def student_profile(id):

    student = Student.query.get_or_404(id)

    return render_template("student_profile.html", student=student)


@app.route("/students/add", methods=["GET", "POST"])
@login_required
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
@login_required
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

    return render_template(
        "edit_student.html",
        student=student,
    )


@app.route("/students/delete/<int:id>")
@login_required
def delete_student(id):

    if current_user.role != "admin":
        flash(
            "You do not have permission to delete students.",
            "danger",
        )

        return redirect(url_for("students"))

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    flash("Student deleted successfully!", "success")

    return redirect(url_for("students"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)

            flash("Welcome back!", "success")

            return redirect(url_for("home"))

        flash(
            "Invalid username or password.",
            "danger",
        )

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Logged out successfully.",
        "success",
    )

    return redirect(url_for("login"))


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
