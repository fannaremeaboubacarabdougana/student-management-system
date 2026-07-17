from app import app
from models import db, User

with app.app_context():
    # Check if the staff user already exists
    existing_staff = User.query.filter_by(username="staff").first()

    if existing_staff:
        print("Staff user already exists.")
    else:
        staff = User(username="staff", email="staff@example.com", role="staff")

        staff.set_password("staff123")

        db.session.add(staff)
        db.session.commit()

        print("Staff user created successfully!")
