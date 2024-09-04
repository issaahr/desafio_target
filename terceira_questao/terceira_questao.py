import json

def calcular_menor_maior_faturamento(dados):
    """Calcula o menor e o maior valor de faturamento da lista de dados."""
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    if not valores:
        return None, None
    
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    
    return menor_faturamento, maior_faturamento

def calcular_media_e_dias_acima(dados):
    """Calcula a média mensal e o número de dias com faturamento acima da média."""
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    if not valores:
        return 0, 0
    
    media_faturamento = sum(valores) / len(valores)
    dias_acima_media = sum(1 for dia in dados if dia['valor'] > media_faturamento)
    
    return media_faturamento, dias_acima_media


# Caminho para o arquivo JSON
caminho_arquivo = 'terceira_questao/dados.json'
    
# Carregar os dados do arquivo JSON diretamente
try:
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    print(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
    
# Calcular menor e maior faturamento
menor_faturamento, maior_faturamento = calcular_menor_maior_faturamento(dados)
    
# Calcular média mensal e dias acima da média
media_faturamento, dias_acima_media = calcular_media_e_dias_acima(dados)
    
# Exibir os resultados
print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")