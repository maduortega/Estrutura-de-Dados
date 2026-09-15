from collections import deque
from Capsula import Capsula
from random import randint

def adicionar(fila):
    while True:
        serie = int(input('Informe o número de série da capsula: '))
        volume = randint(20,100) # Volume de O² da capsula
        
        if serie <= 0:
            print('Número de série inválido.')
            continue
        break
        
    fila.append(Capsula(serie, volume))
    print(f'A capsula N°{serie} acoplada com sucesso!')
    
def consumir(fila, arquivos):
    if not fila: # Se a fila estiver vazia
        print('⚠ ALERTA VERMELHO ⚠ - ERRO AO CONSUMIR, NAVE SEM O² ACOPLADO')
        return # Tentar consumir sem oxigênio é um alerta vermelho
    else:
        print('Liberando capsula para consumo...')
        cons = fila.popleft()
        print(f'Capsula consumida com sucesso --> {cons}')
        arquivos.append(cons) # Recebe o objeto capsula
    
def monitorar(fila):
    if not fila: # Se a fila estiver vazia
        print('Os trilhos de suprimentos estão vazios.')
        return # Ao apenas monitorar, não é um alerta vermelho
    else:
        print('Capsulas restantes para processamento...')
        for item in fila:
            print(f'Capsula N° {item.serie}, Volumetria de O² {item.volume}')
            
        print(f'Total de capsulas restantes: {len(fila)}')
        
def relatar(fila, arquivos):
    total_02 = 0
    qtd_cap = 0
    
    if fila: # Se a fila ainda estiver cheia
        print('O trilho de suprimentos não está vazio. O relatório não pode ser concluído.')
        return
    if not arquivos: # Se tentar rodar os arquivos sem ter nada (escolher essa opção 1°)
        print('Não há arquivos para serem processados')
        return
    else:
        print('Relátorio de O² da nave Selmininin-BX29...')

        for itens in arquivos:
            total_02 += itens.volume
        qtd_cap = len(arquivos)
        media = total_02 / qtd_cap
        
        print(f'Total de O² da nave: {total_02} | Capsulas processadas: {qtd_cap} | Média de O² por capsula: {media}')
        print('Relatório finalizado com sucesso.')  

def gerar_menu():
    print()
    print('[1] Adicionar capsula de O²')
    print('[2] Consumir capsula de O²')
    print('[3] Monitorar trilho de suprimentos')
    print('[4] Relatório de oxigênio da nave')
    print('[5] Finalizar')
    print()

def main():
    fila = deque() # A fila deve ficar no main para que ela não seja resetada sempre
    arquivos = [] # Tudo que for consumido fica registrado na lista de arquivos
    
    while True:
        gerar_menu()
        opcao = int(input('Informe uma opção --> '))
        print()
        
        match opcao:
            case 1:
                adicionar(fila)
            case 2:
                consumir(fila, arquivos)
            case 3:
                monitorar(fila)
            case 4:
                relatar(fila, arquivos)
            case 5:
                print('Finalizado!')
                break
            case _:
                print('Informe uma opção válida')
    
if __name__ == '__main__':
    main()