from app import db

class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    edition = db.Column(db.String(50))
    availability = db.Column(db.String(50))