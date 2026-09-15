from collections import deque

def binario(n: int):
    pilha = deque()
    binario = []
    aux = n
    
    while aux > 0:
        resto = 0
        resto = aux % 2
        aux = aux // 2
        
        pilha.append(resto)
    
    while pilha:
        binario.append(pilha.pop()) # Vai retirando da pilha e colocando na lista
        
    return binario

def main():
    while True:
        n = int(input('Informe um número --> '))
        if n < 0:
            print('O número deve ser positivo')
        
        resp = binario(n)
        print(f'Número convertido em binário --> {resp}')
        print()

if __name__ == '__main__':
    main()