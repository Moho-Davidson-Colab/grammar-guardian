import certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
load_dotenv()

def get_collection():
    uri = os.getenv('MONGO_URI')
    try:
        client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
        print("Pinged your deployment. You successfully connected to MongoDB!")
        db = client.get_database('sample_mflix')
        collection = db["test"]
        return collection
    except Exception as e:
        print(e)
        return collection
