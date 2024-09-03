def calculo_fibonacci(numero):
    a = 0
    b = 1

    while a <= numero: 
        if a == numero:
            return True
        # Atualiza os valores de a e b
        c = a + b
        a = b
        b = c
    return False

# Solicita o número ao usuário
numero_informado = int(input("Digite o número para saber se ele pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência e imprime o resultado
if calculo_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
