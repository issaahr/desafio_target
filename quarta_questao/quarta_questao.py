faturamento_estados = [
    {"estado": "SP", "valor": 67836.43},
    {"estado": "RJ", "valor": 36678.66},
    {"estado": "MG", "valor": 29229.88},
    {"estado": "ES", "valor": 27165.48},
    {"estado": "Outros", "valor": 19849.53}
]

# Cálculo do faturamento total
faturamento_total = sum(estado['valor'] for estado in faturamento_estados)

# Cálculo do percentual de cada estado
for estado in faturamento_estados:
    percentual = (estado['valor'] / faturamento_total) * 100
    estado['percentual'] = percentual

# Exibição dos resultados
for estado in faturamento_estados:
    if estado['estado'] == "Outros":
        print(f"A soma do faturamento dos outros estados representa {estado['percentual']:.2f}% do faturamento total.")
    else:
        print(f"O estado {estado['estado']} representa {estado['percentual']:.2f}% do faturamento total.")