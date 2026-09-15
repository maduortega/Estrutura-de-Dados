from Lista_Dupla import Lista_Dupla

# Algoritmo de ordenação
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
    lista = Lista_Dupla()
    
    tamanho = int(input('Informe o tamanho da lista: '))
    print()
    
    for _ in range(tamanho):
        n = int(input('Informe um número: '))
        lista.add_final(n)
    print()
    
    insertion_sort(lista) # Chama a função
    lista.imprimir() # Imprime a lista depois da função terminar

if __name__ == '__main__':
    main()