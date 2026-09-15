from Lista_Dupla import Lista_Dupla

def intercalar(Lista1: Lista_Dupla, Lista2: Lista_Dupla) -> Lista_Dupla:
    ListaNova = Lista_Dupla()
    p1 = Lista1.inicio
    p2 = Lista2.inicio # Ponteiros (aponta pro dado)
    
    while p1 is not None and p2 is not None: # Nossa lista dupla não tem índice
        ListaNova.add_final(p1.dado) # Pega e adiciona o primeiro elemento da lista1
        ListaNova.add_final(p2.dado) # Pega e add primeiro elemento da lista2
        
        p1 = p1.dir
        p2 = p2.dir # Depois de add, pega o próximo
    
    # Ainda há elementos na lista 1? | Quando as duas listas não tem o mesmo tamanho
    while p1 is not None:
        ListaNova.add_final(p1.dado) # Se houver números ainda na p1, mas não na p2, adicione.
        p1 = p1.dir # Depois de adicionar, tente pegar o próximo dado
        
    # Ainda há elementos na lista 2? | Quando as duas listas não tem o mesmo tamanho
    while p2 is not None:
        ListaNova.add_final(p2.dado)
        p2 = p2.dir
        
    return ListaNova

def main():    
    Premium = Lista_Dupla()
    Comum = Lista_Dupla()
    
    for _ in range(3):
        Premium.add_final(int(input('Valor para Lista Premium: ')))
    
    for _ in range(3):
        Comum.add_final(int(input('Valor para Lista Comum: ')))
    
    Resultado = intercalar(Premium, Comum)
    Resultado.imprimir()

if __name__ == '__main__':
    main()