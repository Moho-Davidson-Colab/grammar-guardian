from flaskr.models.user import User
from flask import Blueprint, request
from flaskr.test_mongo import get_collection


user_bp = Blueprint('user', __name__)


@user_bp.route('/user', methods=['POST'])
def create_user():
    try:
        user_info = request.get_json()
        user_object = User(**user_info)
        collection = get_collection()
        user_exists = collection.find_one({"userId": user_object.userId})
        if not user_exists:
            user_object.password = user_object.hash_password()
            result = collection.insert_one(user_object.model_dump())
            return "User created successfully", 201
        else:
            return "User already exists", 400
    except Exception as e:
        return str(e), 400
    

@user_bp.route('/login', methods=['POST'])
def login_user():
    try:
        user_info = request.get_json()
        user_object = User(**user_info)
        collection = get_collection()
        user_exists = collection.find_one({"userId": user_object.userId})
        if not user_exists:
            return "User does not exist", 400
        valid_password = user_object.check_password(user_exists['password'])    
        if not valid_password:
            return "Invalid password", 400
        token = user_object.encode_auth_token()
        if token:
            response_object = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': token
            }
            return response_object, 200
        else:
            return "Login failed", 400
    except Exception as e:
        return str(e), 400