from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Diretório onde os arquivos serão armazenados
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Manipulação de listas: Exemplo simples de soma de elementos
@app.route('/sum-list', methods=['POST'])
def sum_list():
    data = request.json
    numbers = data.get('numbers', [])
    total_sum = sum(numbers)
    return jsonify({"sum": total_sum})

# Manipulação de arquivos: Salvar arquivo enviado e retornar o nome do arquivo salvo
@app.route('/upload-file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)
    return jsonify({"filename": file.filename})

# Ler conteúdo de um arquivo e retornar
@app.route('/read-file', methods=['POST'])
def read_file():
    data = request.json
    filename = data.get('filename', '')
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"})
    
    with open(filepath, 'r') as file:
        content = file.read()
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(debug=True)
