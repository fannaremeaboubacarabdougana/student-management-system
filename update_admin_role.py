from app import app
from models import db, User

with app.app_context():
    admin = User.query.filter_by(username="admin").first()

    if admin:
        admin.role = "admin"
        db.session.commit()
        print("Admin role updated successfully!")
    else:
        print("Admin user not found.")
