from collections import deque

def pseudo(lista):
    pilha = deque()
    x = 0
    
    for i in range(len(lista)):
        pilha.append(lista[i])
    
    a = pilha.pop()
    b = pilha.pop()
    
    if a > b:
        x = a
    else:
        x = b
        
    return x

def main():
    lista = []
    
    for _ in range(3):
        n = int(input('Informe um número --> '))
        lista.append(n)
        if n < 0:
            print('O número deve ser positivo')
    print()
        
    resp = pseudo(lista)
    print(f'O possível maior número é: {resp}')

if __name__ == '__main__':
    main()