import requests
import pandas as pd


if __name__ == "__main__":
    # Carrega os dados
    mydf = pd.read_csv('plataformas-cognitivas-local-master/datasets/BaseUnknown03.csv')

    # Filtra alguns para testes:
    filtrados = mydf.sample(7)

    # Prepara chamada
    url = "http://localhost:8081/modelo02"
    headers = {'Content-Type': 'application/json'}
    conteudo = filtrados.to_json(orient='records')

    # Chama API
    response = requests.request("POST", url, headers=headers, data=conteudo)
    
    if response.status_code == 200:
        print("Resposta da API:")
        print(response.json())
    else:
        print("Erro ao chamar a API:", response.status_code)
