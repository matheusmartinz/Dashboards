import requests
import pandas as pd

def obter_dados_da_api(url):
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