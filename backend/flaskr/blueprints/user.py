from flaskr.models.user import User
from flask import Blueprint, request
from flaskr.test_mongo import get_db


user_bp = Blueprint('user', __name__)
db = get_db()
collection = db.get_collection('users')


@user_bp.route('/signup', methods=['POST'])
def signup_user():
    try:
        user_info = request.get_json()
        current_user = User(**user_info)
        user_exists = collection.find_one({"userId": current_user.userId})
        if not user_exists:
            current_user.password = current_user.hash_password()
            result = collection.insert_one(current_user.model_dump())
            token = current_user.encode_auth_token()
            if result.acknowledged and token:
                response_object = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': token
                }
                return response_object, 201
            return "Registration failed", 400
        else:
            return "User already exists", 400
    except Exception as e:
        return str(e), 400


@user_bp.route('/login', methods=['POST'])
def login_user():
    try:
        user_info = request.get_json()
        current_user = User(**user_info)
        user_exists = collection.find_one({"userId": current_user.userId})
        if not user_exists:
            return "User does not exist", 400
        valid_password = current_user.check_password(user_exists['password'])
        if not valid_password:
            return "Invalid password", 400
        token = current_user.encode_auth_token()
        if token:
            response_object = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': token
            }
            return response_object, 200
        return "Login failed", 400
    except Exception as e:
        return str(e), 400
