
from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)


MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client.iot
collection = db.sensors

@app.route('/data', methods=['POST'])
def add_data():
    data = request.json or {}
    collection.insert_one(data)
    return jsonify({"status": "ok"}), 201

@app.route('/data', methods=['GET'])
def get_data():
    docs = list(collection.find({}, {'_id': 0}))
    return jsonify(docs)

@app.route('/', methods=['GET'])
def root():
    return jsonify({"hello": "iot-cloud", "endpoints": ["/data (GET/POST)"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
