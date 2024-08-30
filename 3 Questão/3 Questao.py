import json

def processar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    faturamento = dados['faturamento']
    
    valores = [item['valor'] for item in faturamento if item['valor'] > 0]
    
    if not valores:
        return "Não há dados de faturamento para processar."

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)

    dias_acima_da_media = sum(1 for item in faturamento if item['valor'] > media_mensal)

    resultado = {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

    return resultado

arquivo_json = 'C:/Users/xriga/Documents/Projetos/EstagioProvaTecnica/3 Questão/faturamento.json'

resultado = processar_faturamento(arquivo_json)
print(f"Menor faturamento: {resultado['menor_faturamento']}")
print(f"Maior faturamento: {resultado['maior_faturamento']}")
print(f"Número de dias acima da média: {resultado['dias_acima_da_media']}")
