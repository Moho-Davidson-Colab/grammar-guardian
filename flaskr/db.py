import sqlite3

import click
from flask import current_app, g
import certifi


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://nhuy52913:KqjPEcmg98qpRdXo@cluster0.rsy5qtv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)