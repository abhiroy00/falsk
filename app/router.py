from flask import Blueprint, jsonify, request
from app.model import User

router = Blueprint('router', __name__)

@router.route('/register', methods=["GET"])
def register():
    if request.method == "GET":
        # Fetch all users from the database
        user_data = User.query.all()
        # Serialize the user data
        user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in user_data]
        return jsonify(user_list)
    return jsonify({"error": "Method not allowed"}), 405

