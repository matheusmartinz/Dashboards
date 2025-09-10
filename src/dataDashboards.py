import pandas as pd
import re
import api

def soma_valores(text):
    valores = re.findall(r'\d+\.\d+', text)
    return sum(float(v) for v in valores)

def loadDataLogistica():
    DF_logistica = api.fetch_Json_data('dados/Logistica.json')

    DF_logistica = DF_logistica.rename(columns={'ID Entrega': 'Código Entrega', 'Peso (kg)': 'Peso'})
    DF_logistica['Data Saída'] = pd.to_datetime(DF_logistica['Data Saída'], errors='coerce')
    
    DF_logistica['Custo Frete'] = (
        DF_logistica['Custo Frete']
        .str.replace('R\$ ', '', regex=True)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
        .astype(float)
    )

    DF_logistica = DF_logistica[DF_logistica['Custo Frete'] > 0]
    
    DF_logistica = DF_logistica.sort_values(by='Data Saída')
    
    return DF_logistica

def loadDataVendas():
    DF = api.fetch_Json_data('dados/Vendas.json')

    DF['Valor Final'] = DF['Valor Final'].apply(soma_valores)
    DF['Valor Unitário'] = DF['Valor Unitário'].apply(soma_valores)
    DF['Data'] = pd.to_datetime(DF['Data'], errors='coerce')
    DF = DF.rename(columns={'ID Loja': 'Região Lojas'})

    DF_filtered_table = DF.loc[:, ["Data", "Produto", "Valor Final"]]
    DF_filtered_table['Data'] = DF_filtered_table['Data'].dt.strftime('%d/%m/%Y')

    DF_grouped = DF.groupby(['Data', 'Produto'], as_index=False)['Valor Final'].sum()
    max_valor = DF_grouped['Valor Final'].max()

    DF_line = DF.groupby(['Data', 'Região Lojas'], as_index=False)['Valor Unitário'].sum()
    max_valor_line = DF_line['Valor Unitário'].max()

    return {
        "DF": DF,
        "DF_filtered_table": DF_filtered_table,
        "DF_grouped": DF_grouped,
        "DF_line": DF_line
    }