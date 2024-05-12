from flaskr.models.user import User
from flask import Blueprint, request

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    user_info = request.get_json()
    user_object = User(**user_info)
    return user_object.model_dump()