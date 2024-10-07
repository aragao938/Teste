def fibonacci_sequence(n):
    # Função que gera os primeiros n valores da sequência de Fibonacci.
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_fibonacci(number, sequence):
    # Verifica se o número está na sequência de Fibonacci fornecida.
    return number in sequence

# Solicitando ao usuário o número a ser verificado
number = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Gerando os primeiros 20 valores da sequência de Fibonacci
fibonacci_20 = fibonacci_sequence(20)
print("Sequência de Fibonacci gerada:", fibonacci_20)

# Verificando se o número informado pertence à sequência de Fibonacci
if is_fibonacci(number, fibonacci_20):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")
