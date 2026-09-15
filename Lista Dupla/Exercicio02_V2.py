from Lista_Dupla import Lista_Dupla
from random import randint

def deslocar(Lista: Lista_Dupla, desl: int):
    # Não há rotação?
    if desl == 0 or desl == Lista.tamanho or Lista.tamanho == 1:
        return # Vaza da função, retorna a lista sem modificações
    
    # Calcula o valor do deslocamento enquanto n for maior que o tamanho
    desl = desl % Lista.tamanho
    
    # Se o valor de deslescolamento for múltiplo, não rotaciona
    if desl == 0:
        return
    
    # Auxiliar para percorrer a lista e encontrar o "novo" início
    aux = Lista.inicio
    for _ in range(desl):
        aux = aux.dir
        
    # Configura o novo início e o novo fim
    novo_inicio = aux
    novo_fim = aux.esq
    
    # Cortando as antigas ligações (pois o final não tem próximo e início não tem anterior)
    novo_inicio.esq = None
    novo_fim.dir = None
    
    # Trocando os ponteiros do fim e início, que agora apontam pra dados diferentes
    # Final aponta pro próximo deslocado, enquanto o próximo aponta (esquerda) para o antigo final
    Lista.fim.dir = Lista.inicio
    Lista.inicio.esq = Lista.fim
    
    # Trocando o fim e o começo (deslocando)
    Lista.fim = novo_fim
    Lista.inicio = novo_inicio

def main():
    Lista = Lista_Dupla()
    tamanho = int(input('Escolha o tamanho da lista: '))
    
    for _ in range(tamanho):
        Lista.add_final(int(input('Informe um valor: '))) # Ou randint
        
    desl = randint(0, tamanho * 2)
    print(f'O deslocamento será de: {desl}')
    
    deslocar(Lista, desl)
    print()
    Lista.imprimir()

if __name__ == '__main__':
    main()