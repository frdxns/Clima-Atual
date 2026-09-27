import requests, os, json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"


def clima_local(cidade):
    params = {
        "key": API_KEY,
        "q": cidade,
        "lang": "PT"
    }

    resposta = requests.get(URL, params=params)

    if resposta.status_code == 200:
        dados = resposta.json()

    dadoscompleto = {
            "local": dados["location"]["name"],
            "temperatura": dados["current"]["temp_c"],
            "descricao": dados["current"]["condition"]["text"],
            "vento": dados["current"]["wind_kph"],
            "umidade": dados["current"]["humidity"],
            "chuva": dados["current"]["chance_of_rain"],
            "hora": dados["location"]["localtime"].split(' ')[1],
        }

    dados_local = json.dumps(dadoscompleto)
    return dados_local

    