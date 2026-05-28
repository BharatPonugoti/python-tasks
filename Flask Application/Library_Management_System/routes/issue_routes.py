from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.issue_model import IssuedBook
from app import db

issue_bp = Blueprint("issue_bp", __name__)

@issue_bp.route("/api/issue-book", methods=["POST"])
@jwt_required()
def issue_book():

    data = request.get_json()

    issue = IssuedBook(
        client_id=data["client_id"],
        book_id=data["book_id"],
        issue_date=data["issue_date"],
        return_date=data["return_date"],
        late_fee=data["late_fee"]
    )

    db.session.add(issue)
    db.session.commit()

    return jsonify({
        "message": "Book Issued Successfully"
    })