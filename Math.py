from flask import Flask, request, jsonify

global dados

adicionar = 0

global number
global number2

number = [0, 1, 2, 3 ,4 ,5 ,6]
number2 = [7, 8, 9, 10, 11, 12]

for i in range(len(number2), len(number)):
    dados = i

def send_data(a=3, b=5):
    numero = a + b 
    if len(number) < 95:
        number.append(numero)
        number.reverse()
        
    data = {"value": 42}  # Dados de exemplo
    oi = 'helloUnity' # Dados de exemplo
    listaNumber = 'Lista: ', number
    tamanhoNumber = 'Tamanho: ', len(number)
    return jsonify(tamanhoNumber, listaNumber)
