from app import db

class IssuedBook(db.Model):

    __tablename__ = "issued_books"

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    issue_date = db.Column(db.String(20))
    return_date = db.Column(db.String(20))
    late_fee = db.Column(db.Integer)