from flaskr.models.text import Text
from flask import Blueprint, request
from flaskr.test_mongo import get_db

text_bp = Blueprint('text', __name__)
db = get_db()
collection = db.get_collection('texts')

@text_bp.route('/text', methods=['POST'])
def send_text():
    try:
        text_info = request.get_json()
        text_object = Text(**text_info)
        result = collection.insert_one(text_object.model_dump())
        if result.acknowledged:
            response_object = {
                'status': 'success',
                'message': 'Successfully sent text.'
            }
            return response_object, 201
        return "Text sent failed", 400
    except Exception as e:
        return str(e), 400