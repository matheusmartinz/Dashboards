import pandas as pd
import re
import apis.api as api

def soma_valores(text):
    valores = re.findall(r'\d+\.\d+', text)
    return sum(float(v) for v in valores)

def loadDataLogistica():
    DF = api.fetch_Json_data('dados/Logistica.json')

    DF['Data Saída'] = pd.to_datetime(DF['Data Saída'], format='%Y-%m-%d', errors='coerce')
    DF = DF.rename(columns={
        'ID Entrega': 'Código Entrega',
        'Peso (kg)': 'Peso'
    })

    DF['Custo Frete'] = (
        DF['Custo Frete']
        .str.replace('R\$ ?', '', regex=True)
        .str.replace('.', '', regex=False)  
        .str.replace(',', '.', regex=False) 
        .astype(float)
    )
    DF = DF.sort_values(by='Data Saída')
    
    DF_grouped_line = (
        DF.groupby([pd.Grouper(key='Data Saída', freq='D'), 'Tipo de Carga'], as_index=False)['Custo Frete'].sum()
    )
    DF_grouped_line['Custo Frete Formatado'] = DF_grouped_line['Custo Frete'].apply(
    lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
)
    DF_grouped_CDPeso = DF.groupby(['Centro de Distribuição', 'Tipo de Carga'], as_index=False)['Peso'].sum()

    return {
        "DF": DF,
        "DF_grouped_line": DF_grouped_line,
        "DF_grouped_CDPeso": DF_grouped_CDPeso,
    }


def loadDataVendas():
    DF = api.fetch_Json_data('dados/Vendas.json')

    DF['Valor Final'] = DF['Valor Final'].apply(soma_valores)
    DF['Valor Unitário'] = DF['Valor Unitário'].apply(soma_valores)
    DF['Data'] = pd.to_datetime(DF['Data'], errors='coerce')
    DF = DF.rename(columns={'ID Loja': 'Região Lojas'})

    DF_filtered_table = DF.loc[:, ["Data", "Produto", "Valor Final"]]
    DF_filtered_table['Data'] = DF_filtered_table['Data'].dt.strftime('%d/%m/%Y')

    DF_grouped = DF.groupby(['Data', 'Produto'], as_index=False)['Valor Final'].sum()

    DF_line = DF.groupby(['Data', 'Região Lojas'], as_index=False)['Valor Unitário'].sum()

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