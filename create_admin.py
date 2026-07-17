from app import app
from models import db, User

with app.app_context():
    admin = User(username="admin", email="admin@example.com", role="admin")

    admin.set_password("admin123")

    db.session.add(admin)
    db.session.commit()

    print("Admin user created successfully!")
