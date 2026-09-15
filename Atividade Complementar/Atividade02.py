from collections import deque
from Destroco import Destroco
from random import randint

def empilhar(pilha):
    
    nome = input('Informe o nome do destroço: ')
    material = input('Informe o tipo de material: ')
    valor = randint(0,100) # Gera um valor aleatório para o material
    
    pilha.append(Destroco(nome, material, valor))
    
def analisar(pilha, laboratorio):
    if not pilha: # Se a pilha estiver vazia
        print('Tudo foi analisado! Não há mais nada para o robô retirar.')
        return # Se estiver vazia, para.
    
    print('Próximo item a ser analisado pelo robô alienígena: ')
    extraido = pilha.pop() # Guarda o último item retirado na variável
    laboratorio.append(extraido) # Guarda o objeto na lista
    print(extraido)
    
def verificar(pilha):
    if not pilha: # Se não tiver mais nada para verificar
        print('Missão concluída, itens verificados. Gere o relatório')
        return
    
    for item in pilha:
        print(f'Nome do destroço: {item.nome} | Nome do material: {item.material} | Valor científico: {item.valor}')
    
    print()
    print(f'Camadas restantes para análise: {len(pilha)}') # Mostra o tamanho atual da pilha

def relatar(pilha, laboratorio):
    total_valor = 0
    total_itens = 0
    
    if pilha: # Se a pilha ainda estiver com destroços
        print('A pilha não está vazia! Quase desmoronou em cima da sua nave.')
        return
        
    if not laboratorio: # Se tentar acessar o lab vazio (escolher como 1° opção)
        print('Não há nada que tenha sido analisado ainda.')
        return
    
    else:
        print('Análise alienígena em processamento...')
        
        for itens in laboratorio:
            total_valor += itens.valor # Acessa o valor do material
        total_itens = len(laboratorio) # Tamanho da lista é a quantidade de itens analisados
        
        print(f'Total de itens analisados: {total_itens} | Valor científico da expedição: {total_valor}')
        print('Missão Selmininin-BX29 finalizada com sucesso 🛸')
            
def gerar_menu():
    print()
    print('[1] Adicionar destroço no topo')
    print('[2] Analisar topo')
    print('[3] Verificar pilha completa')
    print('[4] Relatório expedição')
    print('[5] Finalizar')
    print()

def main():
    pilha = deque() # A pilha deve ficar no main para que ela não seja resetada sempre
    laboratorio = [] # Tudo que for analisado vai para a lista do laboratório
    
    while True:
        gerar_menu()
        opcao = int(input('Informe uma opção --> '))
        print()
        
        match opcao:
            case 1:
                empilhar(pilha)
            case 2:
                analisar(pilha, laboratorio)
            case 3:
                verificar(pilha)
            case 4:
                relatar(pilha, laboratorio)
            case 5:
                print('Finalizado!')
                break
            case _:
                print('Informe uma opção válida')
    
if __name__ == '__main__':
    main()