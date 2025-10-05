# Flask: hafif bir web framework
# PyMongo: MongoDB'ye Python’dan bağlanmamızı sağlar
# os: ortam değişkenlerini (ENV) okumak için
from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MONGO_URI'yi ENV üzerinden al (K8s/Docker'da gerektiği gibi override edebiliriz)
# Varsayılan: docker ağı içinde 'mongo' ismiyle koşan servise 27017 portundan bağlan
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client.iot
collection = db.sensors

# POST /data: sensör verisini al, MongoDB'ye yaz
@app.route('/data', methods=['POST'])
def add_data():
    data = request.json or {}
    collection.insert_one(data)
    return jsonify({"status": "ok"}), 201

# GET /data: MongoDB'deki tüm kayıtları JSON olarak döndür
@app.route('/data', methods=['GET'])
def get_data():
    # _id alanını gizliyoruz (JSON'a uyuşmuyor ve burada işimiz yok)
    docs = list(collection.find({}, {'_id': 0}))
    return jsonify(docs)

# GET /: basit sağlık/test endpoint'i
@app.route('/', methods=['GET'])
def root():
    return jsonify({"hello": "iot-cloud", "endpoints": ["/data (GET/POST)"]})

if __name__ == '__main__':
    # 0.0.0.0: container dışından ulaşılabilir olsun
    app.run(host='0.0.0.0', port=5000)
