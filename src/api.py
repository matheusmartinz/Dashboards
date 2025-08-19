import requests
import pandas as pd
import json

def fetch_data(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                DF = pd.DataFrame(data)
                return DF
            else:
                print(f"Erro na requisição: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None

def fetch_Json_data(filePath: str):
    try:
        with open(filePath, 'r', encoding="utf-8") as file:
            dataVendas = json.load(file)
        return pd.DataFrame(dataVendas);
    except FileNotFoundError:
        raise RuntimeError("Arquivo JSON não encontrado.")
    except json.JSONDecodeError:
        raise RuntimeError("Erro ao decodificar o arquivo JSON.")