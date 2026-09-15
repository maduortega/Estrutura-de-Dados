from ListaDupla import ListaDupla
from ListaDupla import No
from Devedor import Devedor

def adicionar(lista):
    while True:
        aux = lista.inicio
        
        nome = input('Informe o nome do devedor: ')
        divida = float(input('Informe o valor da dívida: '))
        
        if divida <= 0:
            print('Valor da dívida inválido.')
            continue # Pede pra informar novamente
        break # Encerra se tudo estiver ok
    
    novo = No(Devedor(nome, divida))
            
    if lista.tamanho == 0: # Não há elementos ainda
        lista.add_final(Devedor(nome, divida))
        return # Inseriu, parou.

    while aux:
        if aux.dado.divida >= novo.dado.divida and aux.esq is None: # Não há elemento anterior
            aux.esq = novo
            novo.dir = aux
            novo.esq = None
            lista.inicio = novo # Novo início (igual o método add_inicio faz)
            
            lista.tamanho += 1
            return
            
        elif aux.dado.divida >= novo.dado.divida and aux.esq is not None: # Inserir no meio
            aux.esq.dir = novo
            novo.esq = aux.esq
            aux.esq = novo
            novo.dir = aux
            
            lista.tamanho += 1
            return
            
        elif aux.dir is None: # O novo valor é maior do que todos os existentes, coloca no fim
            lista.add_final(Devedor(nome, divida))
            return
    
        aux = aux.dir
        
    
def pagar(lista):
    while True:
        aux = lista.inicio # Pra resetar a cada busca tem que estar no while true
        cont = 0
        nome = input('Informe o nome do devedor: ')
        
        while aux:
            if aux.dado.nome == nome:
                cont = 1
                
                print(aux.dado, end='\n')
                nmdev = int(input('Este é o devedor que estava procurando? 1 - Sim | 2 - Não: '))
                
                if nmdev == 2:
                    break
                elif nmdev == 1:
                    pag = float(input('Digite o valor do pagamento --> '))
                    
                    if pag <= 0:
                        print('Valor do pagamento inválido.')
                        continue
                    elif pag >= aux.dado.divida:
                        lista.remover(aux.dado) # Remove o devedor da lista
                        return # Atualizou a dívida, parou.
                    else:
                        aux.dado.divida = aux.dado.divida - pag
                        return
                else:
                    print('Informe uma opção válida.')
                    continue
            
            aux = aux.dir
            
        if cont == 0:
            print('Devedor não encontrado.')
            return # Não achou, parou.
            
def total_devedores(lista):
    aux = lista.inicio
    valor = 0
    
    while aux:
        valor += aux.dado.divida
        aux = aux.dir
    print(f'Total das dívidas dos clientes --> R${valor:.2f}')

def gerar_menu():
    print()
    print('[1] Inserir um novo devedor')
    print('[2] Pagar uma dívida')
    print('[3] Imprimir lista de devedores')
    print('[4] Imprimir total de dívidas dos clientes')
    print('[5] Finalizar')
    print()

def main():
    lista = ListaDupla()
    
    while True:
        gerar_menu()
        opcao = int(input('Informe uma opção --> '))
        print()
        
        match opcao:
            case 1:
                adicionar(lista)
            case 2:
                pagar(lista)
            case 3:
                lista.imprimir()
            case 4:
                total_devedores(lista)
            case 5:
                print('Finalizado!')
                break
            case _:
                print('Informe uma opção válida')
    
if __name__ == '__main__':
    main()
