from Lista_Dupla import Lista_Dupla

def remover_rep(lista):
    aux = lista.inicio
    rep = []
    
    while aux:
        if aux.dado not in rep:
            rep.append(aux.dado)
        else:
            lista.remover(aux.dado)
        aux = aux.dir

def main():
    lista = Lista_Dupla()
    
    tamanho = int(input('Informe o tamanho da lista: '))
    print()
    
    for _ in range(tamanho):
        n = int(input('Informe um número: '))
        lista.add_final(n)
    print()
    
    remover_rep(lista) # Chama a função
    lista.imprimir() # Imprime a lista depois da função terminar

if __name__ == '__main__':
    main()