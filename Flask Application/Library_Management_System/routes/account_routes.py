from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

account_bp = Blueprint("account_bp", __name__)

@account_bp.route("/api/accounts", methods=["GET"])
@jwt_required()
def accounts():

    return jsonify({
        "total_income": 50000,
        "late_fees": 2000,
        "memberships": 48000
    })