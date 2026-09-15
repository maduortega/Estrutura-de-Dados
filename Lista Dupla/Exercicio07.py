from Lista_Dupla import Lista_Dupla

def mesclar(lista1, lista2):
    lista_nova = Lista_Dupla()
    l1 = lista1.inicio
    l2 = lista2.inicio
    
    while l1: 
        lista_nova.add_final(l1.dado)
        l1 = l1.dir # Vai para o próximo
    
    while l2:
        lista_nova.add_final(l2.dado)
        l2 = l2.dir
    
    return lista_nova

def insertion_sort(lista):
    aux = lista.inicio
    
    if aux is None or aux.dir is None:
        return

    # Começa do segundo nó
    no = aux.dir
    while no:
        aux2 = no.dir
        chave = no.dado
            
        # Busca a posição correta na parte ordenada
        procurar = no.esq
        while procurar and procurar.dado > chave:
            procurar = procurar.esq
            
        # Se precisar mover o nó
        if procurar != no.esq:
            # Remove o nó da posição atual
            if no.dir:
                no.dir.esq = no.esq
            no.esq.dir = no.dir
                
            # Insere o nó na posição correta
            if procurar is None: # Inserir no início
                no.dir = aux
                no.esq = None
                aux.esq = no
                aux = no
                lista.inicio = aux  # <-- IMPORTANTE
                
            else: # Inserir entre nós
                no.dir = procurar.dir
                no.esq = procurar
                if procurar.dir:
                    procurar.dir.esq = no
                procurar.dir = no
            
        no = aux2
    lista.inicio = aux

def main():
    lista1 = Lista_Dupla()
    lista2 = Lista_Dupla()
    
    tamanho = int(input('Informe o tamanho das listas: '))
    print()
    
    for _ in range(tamanho):
        n = int(input('Informe um número para a lista 1: '))
        lista1.add_final(n)
    print()
    
    for _ in range(tamanho):
        n = int(input('Informe um número para a lista 2: '))
        lista2.add_final(n)
    print()
    
    lista_nova = mesclar(lista1, lista2) # Chama a função
    insertion_sort(lista_nova)
    
    lista_nova.imprimir()
    

if __name__ == '__main__':
    main()