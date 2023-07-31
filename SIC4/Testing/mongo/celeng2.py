from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Ganti URL dan nama database MongoDB sesuai dengan pengaturan Anda
password = "08b0Qt32zhbwArYG"
uri = f"mongodb+srv://els14029:{password}@sicbatch4.ihzahom.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client['mentor-rusdiansyah'] # ganti sesuai dengan nama database kalian
my_collections = db['arjuna'] 


@app.route('/sensor1/temperature/avg', methods=['GET'])
def get_temperature_avg():
    try:
        # Ambil seluruh data temperature dari database
        data = list(collection.find({}, {'_id': 0, 'temperature': 1}))

        # Hitung nilai rata-rata temperature
        total_temperature = sum(d['temperature'] for d in data)
        avg_temperature = total_temperature / len(data)

        response = {
            'avg_temperature': avg_temperature
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/sensor1/kelembapan/avg', methods=['GET'])
def get_humidity_avg():
    try:
        # Ambil seluruh data kelembapan dari database
        data = list(collection.find({}, {'_id': 0, 'humidity': 1}))

        # Hitung nilai rata-rata kelembapan
        total_humidity = sum(d['humidity'] for d in data)
        avg_humidity = total_humidity / len(data)

        response = {
            'avg_humidity': avg_humidity
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port= 5001, debug=True)
