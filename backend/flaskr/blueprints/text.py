from flaskr.models.text import Text
from flask import Blueprint, request
from flaskr.test_mongo import get_db
from flaskr.nlp.model import generate_text

text_bp = Blueprint('text', __name__)
db = get_db()
collection = db.get_collection('texts')


@text_bp.route('/text', methods=['POST'])
def send_text():
    try:
        text_info = request.get_json()
        current_text = Text(**text_info)
        corrected_text = generate_text(current_text.content)
        result = collection.insert_one(current_text.model_dump())
        if result.acknowledged:
            response_object = {
                'status': 'success',
                'message': 'Successfully sent text.'
            }
            return response_object, 201
        else:
            return 'Failed to send text.', 400
    except Exception as e:
        return str(e), 400
