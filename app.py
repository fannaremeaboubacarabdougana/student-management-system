from flask import Flask, render_template
from config import Config
from models import db
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
