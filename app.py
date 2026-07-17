from flask import Flask, render_template
from config import Config
from models import db, Student
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():

    return render_template("index.html")


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

        return redirect(url_for("home"))

    return render_template("add_student.html")


@app.route("/students")
def students():

    students = Student.query.all()

    return render_template("students.html", students=students)


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
