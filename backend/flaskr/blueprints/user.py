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
        user_exists = collection.find_one({"username": current_user.username})
        if not user_exists:
            current_user.password = current_user.hash_password()
            result = collection.insert_one(current_user.model_dump())
            access_token = User.encode_auth_token(
                current_user.username, "access_token")
            refresh_token = User.encode_auth_token(
                current_user.username, "refresh_token")
            if result.acknowledged and access_token and refresh_token:
                response_object = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
                return response_object, 201
            return "Registration failed", 400
        else:
            return "User already exists", 400
    except Exception as e:
        return e, 400


@user_bp.route('/signin', methods=['POST'])
def login_user():
    try:
        user_info = request.get_json()
        current_user = User(**user_info)
        user_exists = collection.find_one({"username": current_user.username})
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


@user_bp.route('/refresh', methods=['POST'])
def refresh_token():
    try:
        access_token = request.get_json()['access_token']
        refresh_token = request.get_json()['refresh_token']
        access_result = User.decode_auth_token(access_token)
        # If access token is invalid or expired, try to refresh it
        if access_result == 'Signature expired. Please log in again.':
            refresh_result = User.decode_auth_token(refresh_token)
            # If refresh token is invalid or expired, ask user to log in again
            if refresh_result == 'Invalid token. Please log in again.' or refresh_result == 'Signature expired. Please log in again.':
                return {'status': 'fail', 'message': 'Invalid or expired refresh token. Please log in again.'}, 401
            username = refresh_result['sub']
            new_access_token = User.encode_auth_token(username, "access_token")
            response_object = {
                'status': 'success',
                'message': 'Token refreshed.',
                'access_token': new_access_token,
                'refresh_token': refresh_token
            }
            return response_object, 200
        if access_result == 'Invalid token. Please log in again.':
            return {'status': 'fail', 'message': 'Invalid or expired access token. Please log in again.'}, 401
        else:
            response_object = {
                'status': 'success',
                'message': 'No refresh needed.',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            return response_object, 200
    except Exception as e:
        return str(e), 400
