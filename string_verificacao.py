# Solicita ao usuário uma string
user_string = input("Informe uma string: ")

# Conta as ocorrências das letras 'a' e 'A'
count_a = user_string.count('a') + user_string.count('A')

# Verifica se a letra 'a' (maiúscula ou minúscula) está presente e imprime o resultado
if count_a > 0:
    print(f"A letra 'a' (maiúscula ou minúscula) ocorre {count_a} vezes na string.") #O código não reconhece se houver acentuação no a
else:
    print("A letra 'a' (maiúscula ou minúscula) não está presente na string.")
