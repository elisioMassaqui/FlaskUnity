from flask import Flask, request, jsonify
from Math import send_data

app = Flask(__name__)

global dados

adicionar = 0

global number
global number2

number = [0, 1, 2, 3 ,4 ,5 ,6]
number2 = [7, 8, 9, 10, 11, 12]

for i in range(len(number2), len(number)):
    dados = i

@app.route('/service', methods=['GET'])
def service():
    return jsonify('Conectado ao Flask')

# Endpoint para receber dados do Unity
@app.route('/data', methods=['POST'])
def receive_data():
    number.clear()
    if request.is_json:
        data = request.get_json()
    if data == {"key":"value"}:
        print("Dados recebidos:", data)
        return jsonify({"status": "sucesso"})
    else:
        return jsonify({"error": "Tipo de mídia não suportado"}), 415

# Endpoint para enviar dados ao Unity
@app.route('/data', methods=['GET'])
def enviar():
    return send_data()

if __name__ == '__main__':
    app.run(port=5000)
