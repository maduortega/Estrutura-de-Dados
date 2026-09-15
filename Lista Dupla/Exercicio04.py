from Lista_Dupla import Lista_Dupla

def tem_ciclo(lista):
    t = lista.inicio
    l = lista.inicio
    cont = 0
    
    while t.dir is not None and l.dir.dir is not None:
        if cont != 0:
            if t.dado == l.dado:
                return True
        t = t.dir.dir # Anda 2
        l = l.dir # Anda 1
        cont = 1
    return False
 
def main():
    lista = Lista_Dupla()
    
    # Adicionando valores na lista para teste
    lista.add_inicio(5)
    lista.add_inicio(2)
    lista.add_inicio(3)
    lista.add_final(7)
    
    # Fazendo a lista ter ciclo
    lista.fim.dir = lista.inicio # O final aponta para o inicio, vira um ciclo
    
    # Mostra o resultado
    print()
    resul = tem_ciclo(lista)
    print(resul)

if __name__ == '__main__':
    main()