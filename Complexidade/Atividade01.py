# Código O(n)
from random import randint

def main():
    lista = []
    lista_nova = []
    soma = 0
    
    for _ in range(1, 10):
        lista.append(randint(1,20))
        
    for i in range(len(lista)):
        soma = soma + lista[i]
        media = round(soma / (i+1), 2)
        lista_nova.append(media)
        
    print(lista)
    print(lista_nova)
    
if __name__ == '__main__':
    main()