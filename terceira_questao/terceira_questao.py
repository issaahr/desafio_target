import json

def analisar_faturamento(dados):
    # Filtrar apenas os dias com faturamento
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    if not faturamentos:
        return None, None, 0

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)
    
    dias_acima_da_media = sum(1 for dia in dados if dia['valor'] > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():
    # Caminho para o arquivo JSON
    caminho_arquivo = 'dados.json'
    
    # Ler dados do arquivo JSON
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    
    # Analisar os dados
    menor, maior, dias_acima = analisar_faturamento(dados)

    # Exibir resultados
    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")
    print(f"Número de dias com faturamento acima da média: {dias_acima}")

if __name__ == "__main__":
    main()
