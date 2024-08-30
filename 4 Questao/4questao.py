def calcular_percentual(faturamento_estados):
    total_faturamento = sum(faturamento_estados.values())
    
    percentual_representacao = {
        estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()
    }
    
    return percentual_representacao

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 35678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OUTROS": 19849.53
}

percentuais = calcular_percentual(faturamento_estados)

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
