from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.client_model import Client
from app import db

client_bp = Blueprint("client_bp", __name__)

@client_bp.route("/api/clients", methods=["GET"])
@jwt_required()
def get_clients():

    clients = Client.query.all()

    output = []

    for client in clients:
        output.append({
            "id": client.id,
            "name": client.client_name,
            "mobile": client.mobile,
            "premium_status": client.premium_status
        })

    return jsonify(output)


@client_bp.route("/api/clients", methods=["POST"])
@jwt_required()
def add_client():

    data = request.get_json()

    new_client = Client(
        client_name=data["client_name"],
        mobile=data["mobile"],
        premium_status=data["premium_status"]
    )

    db.session.add(new_client)
    db.session.commit()

    return jsonify({
        "message": "Client Added"
    })