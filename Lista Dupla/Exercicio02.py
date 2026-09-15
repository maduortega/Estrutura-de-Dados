from Lista_Dupla import Lista_Dupla

def deslocar(Lista, desl):
# Não podemos ter uma aux p1, pois o valor da p1 não é atualizado conforme o for anda
# Ou seja, continua sendo o mesmo primeiro valor pra qualquer deslocamento.
    if desl == 0:
        return Lista
    
    else:
        for _ in range(desl):
            Lista.add_final(Lista.inicio.dado) # Adiciona o primeiro dado no final da lista
            Lista.remover(Lista.inicio.dado)
        
    # Não precisamos de p1 = p1.dir pois o for se atualiza sozinho
    return Lista

def main():
    Lista = Lista_Dupla()
    tamanho = int(input('Escolha o tamanho da lista: '))
    
    for _ in range(tamanho):
        Lista.add_final(int(input('Informe um valor: ')))
        
    desl = int(input('Informe quantos elementos deseja deslocar: ')) % Lista.tamanho
    
    Listinha = deslocar(Lista, desl) # Temos que fazer isso pois retornamos
    Listinha.imprimir() # Caso contrário só fariamos --> lista.imprimir()

if __name__ == '__main__':
    main()