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
        result = collection.insert_one(user_object.model_dump())
        print(result.acknowledged)
        print("test")
        return user_object.model_dump()
    except Exception as e:
        return str(e), 400