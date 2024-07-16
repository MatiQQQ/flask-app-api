from app import app, db
from models import User  # Import your models here


def create_db():
    with app.app_context():
        db.create_all()
        print("Database tables created")


if __name__ == "__main__":
    create_db()
