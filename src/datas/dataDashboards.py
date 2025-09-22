import pandas as pd
from utils.formaterToNumber import formaterToNumber
from utils.formaterToReal import formaterToReal
from utils.formaterDate import formaterDate
from collections import Counter
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
    DF_line['Data'] = DF_line['Data'].dt.strftime('%Y-%m-%d')

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
    
def loadDataElite():
    DF = api.fetch_Json_data('dados/Elite.json')  
    
    if DF.empty:
        return {'detalhes': [], 'resumo': {}}

    detalhes = []
    resumo = {}

    for colecao, grupo in DF.groupby('colecao'):
        total = int(grupo['numero_modelos'].iloc[0])
        
        tabela_modelos = []
        
        for _, row in grupo.iterrows():
            modelos = row['modelos']

            if not isinstance(modelos, list):
                modelos = [modelos]

            for modelo_info in modelos:
                status = modelo_info.get("status", "").strip().upper()
                linha = {
                    "colecao": colecao,
                    "numero_modelos": total,
                    "modelo": modelo_info.get("modelo"),
                    "status": status
                }
                tabela_modelos.append(linha)

        detalhes.extend(tabela_modelos)

        status_list = [item['status'] for item in tabela_modelos]
        contagem = Counter(status_list)
        
        resumo[colecao] = {
            "Coleção": colecao,
            "Previsto": total,
            "Criados": len(tabela_modelos),
            "Não iniciado": contagem.get("NÃO INICIADO", 0),
            "Desenvolvimento": contagem.get("EM DESENVOLVIMENTO", 0),
            "Aprovado": contagem.get("APROVADO", 0),
            "Reprovado": contagem.get("REPROVADO", 0),
            "Cancelado": contagem.get("CANCELADO", 0),
        }
        
        for key in ["Criados", "Não iniciado", "Desenvolvimento", "Aprovado", "Reprovado", "Cancelado"]:
            resumo[colecao][f"{key} %"] = f"{(resumo[colecao][key] / total * 100):.2f}%" if total > 0 else "0.00%"
        
        for key in ["Criados", "Não iniciado", "Desenvolvimento", "Aprovado", "Reprovado", "Cancelado"]:
            resumo[colecao][key] = f"{resumo[colecao][key]} ({resumo[colecao][f'{key} %']})"
            
        for colecao in resumo:
            for key in ["Criados %", "Não iniciado %", "Desenvolvimento %", "Aprovado %", "Reprovado %", "Cancelado %"]:
                if key in resumo[colecao]:
                 del resumo[colecao][key]
    return {
        'detalhes': detalhes,
        'resumo': list(resumo.values())
    }