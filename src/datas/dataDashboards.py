import pandas as pd
from utils.formaterToNumber import formaterToNumber
from utils.formaterToReal import formaterToReal
from utils.formaterDate import formaterDate
import re
import apis.api as api

def loadDataLogistica():
    DF = api.fetch_Json_data('dados/Logistica.json')

    DF['Data Saída'] = pd.to_datetime(DF['Data Saída'], format='%Y-%m-%d', errors='coerce')
    DF = DF.rename(columns={
        'ID Entrega': 'Código Entrega',
        'Peso (kg)': 'Peso'
    })

    DF['Custo Frete'] = formaterToNumber(DF['Custo Frete'])
    DF = DF.sort_values(by='Data Saída')
    
    DF_grouped_line = (
        DF.groupby([pd.Grouper(key='Data Saída', freq='D'), 'Tipo de Carga'], as_index=False)['Custo Frete'].sum()
    )

    DF_grouped_line['Custo Frete Formatado'] = formaterToReal(DF_grouped_line['Custo Frete'])
    DF_grouped_CDPeso = DF.groupby(['Centro de Distribuição', 'Tipo de Carga'], as_index=False)['Peso'].sum()

    return {
        "DF": DF,
        "DF_grouped_line": DF_grouped_line,
        "DF_grouped_CDPeso": DF_grouped_CDPeso,
    }


def loadDataVendas():
    DF = api.fetch_Json_data('dados/Vendas.json')
    
    DF['Data'] = pd.to_datetime(DF['Data'], errors='coerce')
    DF['Valor Final'] = formaterToNumber(DF['Valor Final'])
    DF['Valor Final View'] = formaterToReal(DF['Valor Final'])
    DF['Custo Frete'] = formaterToNumber(DF['Custo Frete'])
    DF = DF.rename(columns={'ID Loja': 'Região Lojas'})

    DF_filtered_table = DF.loc[:, ["Data", "Produto", "Valor Final"]]
    DF_filtered_table['Data'] = formaterDate(DF_filtered_table['Data'])
    DF_filtered_table['Valor Final Formatado'] = formaterToReal(DF_filtered_table['Valor Final'])

    DF_grouped = DF.groupby(['Data', 'Produto'], as_index=False)['Valor Final'].sum()
    DF_grouped['Valor Final Formatado'] = formaterToReal(DF_grouped['Valor Final'])
    
    DF_line = (DF.groupby([pd.Grouper(key = 'Data', freq= 'D'), 'Região Lojas'], as_index=False)['Custo Frete'].sum())
    DF_line['Custo Frete Formatado'] = formaterToReal(DF_line['Custo Frete'])

    return {
        "DF": DF,
        "DF_filtered_table": DF_filtered_table,
        "DF_grouped": DF_grouped,
        "DF_line": DF_line
    }
    
def loadDataProducao():
    DF = api.fetch_Json_data('dados/Producao.json')
    
    return {
        'DF': DF
    }