# seeds.py
from app import app
from models import db, Docs, Client, Program
from faker import Faker

with app.app_context():
    fake = Faker()

    # Delete all existing data
    print("Deleting data...")
    Docs.query.delete()
    Client.query.delete()
    Program.query.delete()

    db.session.commit()
    print("Database cleared!")
