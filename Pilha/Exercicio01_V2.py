from collections import deque

def converter(n: int):
    pilha = deque()
    while n > 0:
        pilha.append(n % 2)
        n = n // 2
        
    while pilha:
        print(pilha.pop(), end='')
        
# Programa principal
n = int(input('Informe um valor inteiro e positivo: '))
converter(n)