from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    species = db.Column(db.String(30), nullable=False)
    photo_url = db.Column(db.String(300), nullable=True)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(300), nullable=True)
    available = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"id = {self.id}, name = {self.name}, species = {self.species}, photo_url = {self.photo_url}, age = {self.age}, notes = {self.notes}, available = {self.available}"

