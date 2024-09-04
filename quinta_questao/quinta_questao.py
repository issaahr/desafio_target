# Solicita ao usuário que informe a string e a converte para letras minúsculas
string = input("Digite a string que deseja inverter: ").lower()

# Inicializa a variável que armazenará a string invertida
string_invertida = ""

# Percorre a string original de trás para frente e adiciona cada caractere à string invertida
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

# Exibe a string original e a string invertida
print(f"A string '{string}' invertida fica: '{string_invertida}'")
