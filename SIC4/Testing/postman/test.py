#Import modul yg diperlukan
from flask import Flask
from flask import request

app = Flask(__name__) #menginisialisasi app route

@app.route('/test1', methods=['GET']) #mendefinisikan method yang digunakan
def entry_GET():
    return 'ini metode GET'


@app.route('/test2', methods=['POST']) #mendefinisikan method yang digunakan
def entry_POST():
    params = request.args.get('params')
    param2 = request.args.get('param2')
    return f'ini metode POST dengan parameter sebagai berikut *{params}* dan *{param2}*'


if __name__ == '__main__':
    app.run(port=9090, debug=True)
