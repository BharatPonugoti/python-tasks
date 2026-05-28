from app import db

class Client(db.Model):

    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100))
    mobile = db.Column(db.String(20))
    premium_status = db.Column(db.String(20))