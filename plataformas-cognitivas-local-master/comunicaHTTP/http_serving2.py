import pandas as pd
import json
import numpy as np
from flask import Flask, jsonify, request
import os
import threading

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = NpEncoder

@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(f"Processo server, id: {os.getpid()}, thread: {threading.current_thread().ident}")
    print(request.values)
    return "SERVER IS RUNNING!"

@app.route('/calculadora', methods=['GET'])
def calcular():
    operacao = request.args.get('operacao')
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))

    if operacao == 'soma':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            resultado = num1 / num2
        else:
            return jsonify({'erro': 'Não é possível dividir por zero!'})
    else:
        return jsonify({'erro': 'Operação inválida!'})

    return jsonify({'resultado': resultado,
                    'operacao': operacao,
                    'mensagem': "Obrigado pela chamada de API",
                    'autor': 'Eliezer Junior' 
        })

if __name__ == '__main__':
    print(f"Sou o processo server, id: {os.getpid()}, thread: {threading.current_thread().ident}")
    app.run(port=8080, host='0.0.0.0')
