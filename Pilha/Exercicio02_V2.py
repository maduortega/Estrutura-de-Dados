from collections import deque

def pseudo(lista):
    pilha = deque()
    aux = []
    maior = 0
    
    for i in range(len(lista)):
        pilha.append(lista[i])
    
    while pilha:
        aux.append(pilha.pop()) # Vai tirando da pilha e botando na lista
        
    for i in range(len(aux) - 1): # Vai até aux - 1 pra poder pegar o próximo sem dar erro
        if aux[i] > maior:
            maior = aux[i]
    
    return maior

def main():
    lista = []
    y = int(input('Informe o tamanho da lista: '))
    print()
    
    while True:
        for _ in range(y):
            n = int(input('Informe um número --> '))
            lista.append(n)
            if n < 0:
                print('O número deve ser positivo')
        print()
            
        resp = pseudo(lista)
        print(f'O maior número é: {resp}')
        print()

if __name__ == '__main__':
    main()