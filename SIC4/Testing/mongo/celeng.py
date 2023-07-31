from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Ganti URL dan nama database MongoDB sesuai dengan pengaturan Anda
client = MongoClient('mongodb://localhost:9090/')
db = client['mentor-rusdiansyah'] # ganti sesuai dengan nama database kalian
my_collections = db['arjuna'] # ganti sesuai dengan nama collections kalian


@app.route('/sensor1', methods=['POST'])
def add_sensor_data():
    try:
        # Parsing data dari parameter API
        data = request.get_json()
        temperature = data['temperature']
        humidity = data['humidity']
        timestamp = data.get('timestamp', datetime.now())

        # Simpan data ke database
        sensor_data = {
            'temperature': temperature,
            'humidity': humidity,
            'timestamp': timestamp
        }
        result = collection.insert_one(sensor_data)

        response = {
            'message': 'Data sensor berhasil disimpan!',
            'data_id': str(result.inserted_id)
        }
        return jsonify(response), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port = 9090, debug=True)
