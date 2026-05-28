from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.book_model import Book
from app import db

book_bp = Blueprint("book_bp", __name__)

@book_bp.route("/api/books", methods=["GET"])
@jwt_required()
def get_books():

    books = Book.query.all()

    output = []

    for book in books:
        output.append({
            "id": book.id,
            "book_name": book.book_name,
            "author": book.author,
            "edition": book.edition
        })

    return jsonify(output)


@book_bp.route("/api/books", methods=["POST"])
@jwt_required()
def add_book():

    data = request.get_json()

    new_book = Book(
        book_name=data["book_name"],
        author=data["author"],
        edition=data["edition"],
        availability="Available"
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify({
        "message": "Book Added Successfully"
    })