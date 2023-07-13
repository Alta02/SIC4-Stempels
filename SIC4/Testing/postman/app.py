from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/example', methods=['POST'])
def example_route():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    response = {'message': 'Permintaan diterima', 'name': name, 'age': age}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
