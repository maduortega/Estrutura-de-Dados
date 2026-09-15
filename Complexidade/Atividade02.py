# Código O(n^2)
from random import randint

def repete(lista) -> int:
    nova = []
    achou = 0
    
    for i in lista:
        if i not in nova:
            nova.append(i)
        else:
            achou = i
            break # Quebra todos os laços, mesmo dentro de outro
    if achou is 0:
        return -1
    else:
        return achou

def main():
    lista = []
    
    for _ in range(1, 10):
        lista.append(randint(1,10))
        
    resp = repete(lista)
    print(resp)
    
if __name__ == '__main__':
    main()