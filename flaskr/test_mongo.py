import certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


load_dotenv()
uri = os.getenv('MONGO_URI')

try:
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.get_database('sample_mflix')
    test_collection = db["test_collection"]
    print(db.list_collection_names())
except Exception as e:
    print(e)