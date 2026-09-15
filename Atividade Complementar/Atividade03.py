from collections import deque
from Produto import Produto
from random import randint

def estocar(fila):
    nome = input('Informe o nome do produto: ')
    qtd = int(input('Informe a quantidade: '))
    dt_vali = input('Informe a data de validade: ')

        
    fila.append(Produto(nome, qtd, dt_vali))
    print(f'Produto: {nome} estocado com sucesso!')

def prateleira(fila, gestao):
    if not fila: # Se a fila estiver vazia (sem mais produtos)
        print('Não há mais produtos para serem vendidos!')
        return # Se não houver mais produtos, retorna
    else:
        prat = fila.popleft()
        print(f'Produto colocado para venda! --> {prat}')
        gestao.append(prat) # Recebe o objeto produto

def monitorar(fila):
    if not fila: # Se a fila estiver vazia
        print('Não há produtos no estoque.')
        return
    else:
        print('Produtos no estoque: ')
        for item in fila:
            print(f'Produto: {item.nome}, Quantidade: {item.qtd}, Data de Validade: {item.dt_vali}')
        print()
            
        print(f'Próximo produto para ser colocado na prateleira: {fila[0]}') # Frente da fila

def inspecionar(fila):
    total_item = 0
    contagem = {}
    
    if not fila: # Se a fila estiver vazia
        print('Não há produtos no estoque.')
        return
    
    while True:
        pergunta = int(input('1 - Ver cada produto | 2 - Resumo dos produtos '))
        if pergunta == 1:
            for itens in fila:
                print(f'Produto: {itens.nome} | Quantidade: {itens.qtd} | Validade: {itens.dt_vali}')
            return # Se processou, para
        elif pergunta == 2:
            print()
            print('Inspeção do estoque atual...')
            for prod in fila:
                total_item += prod.qtd
                if prod.nome not in contagem: # Se o produto não estiver no dicionário
                    contagem[prod.nome] = prod.qtd # Como se fosse: {Novo: 1}
                else:
                    contagem[prod.nome] += prod.qtd # Como se fosse: {Atual: +=1}
                    
            for nome, qtd in contagem.items(): # Contagem por item
                print(f'{nome}: {qtd} unidades')
                
            print() 
            print(f'Quantidade total de produtos estocados: {total_item}')
            return
        else:
            print('Opção inválida')
            continue

def relatar(fila, gestao):
    total_item = 0
    custo = 0
    
    if fila: # Se a fila ainda estiver cheia
        print('O estoque ainda não foi esvaziado. Venda tudo antes que estrague!')
        return
    if not gestao: # Caso nenhuma "Venda" tenha sido feita (por na prateleira)
        print('Nenhum produto foi colocado na prateleira ainda')
        return
    else:
        print('Realizando relátorio do mercadinho...')

        for itens in gestao:
            total_item += itens.qtd
            custo += randint(1, 50) # Um item pode custa entre 1 e 50 moedas de ouro
            
        media_ganhos = round(custo / total_item, 2)
        
        print(f'Total de itens vendidos: {total_item} | Total de moedas ganhas {custo} | Média de moedas por item: {media_ganhos}')
        print('Relatório finalizado com sucesso.')  
    
def gerar_menu():
    print()
    print('[1] Adicionar produto no estoque')
    print('[2] Colocar produto na prateleira')
    print('[3] Monitorar estoque')
    print('[4] Inspecionar produtos')
    print('[5] Relatório do mercado')
    print('[6] Finalizar')
    print()

def main():
    fila = deque() # A fila deve ficar no main para que ela não seja resetada sempre
    gestao = [] # Tudo que for feito fica registrado na lista de arquivos
    
    while True:
        gerar_menu()
        opcao = int(input('Informe uma opção --> '))
        print()
        
        match opcao:
            case 1:
                estocar(fila)
            case 2:
                prateleira(fila, gestao)
            case 3:
                monitorar(fila)
            case 4:
                inspecionar(fila)
            case 5:
                relatar(fila, gestao)
            case 6:
                print('Finalizado!')
                break
            case _:
                print('Informe uma opção válida')
    
if __name__ == '__main__':
    main()