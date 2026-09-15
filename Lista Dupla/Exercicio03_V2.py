from Lista_Dupla import Lista_Dupla
from Carro import Carro

def cadastrar(lista):
    qtd = int(input('Quantos carros deseja cadastrar? '))
    
    for _ in range(qtd):
        marca = input('Informe a marca --> ')
        modelo = input('Informe o modelo --> ')
        valor = float(input('Informe o preço --> '))
        
        lista.add_final(Carro(marca, modelo, valor))
        print()
        
def listar(lista):
    lista.imprimir()
    print()
    
def buscar_modelo(lista):
    mdl = input('Informe o modelo para pesquisa: ')
    aux = lista.inicio
    cont = 0
    
    while aux:
        if aux.dado.modelo == mdl:
            print(aux.dado, end='\n')
            cont = 1
        aux = aux.dir
    if cont == 0:
        print('Modelo não encontrado.')
        print()
        
def mais_caro(lista):
    aux = lista.inicio
    valor = 0
    
    while aux:
        if aux.dado.valor >= valor:
            valor = aux.dado.valor
            carro_maiscaro = aux.dado
        aux = aux.dir
    print(f'Carro mais caro --> {carro_maiscaro}')
    
def valor_medio(lista):
    aux = lista.inicio
    soma = 0
        
    while aux:
        soma += aux.dado.valor
        aux = aux.dir
    media = round(soma / lista.tamanho, 2)
    print(f'Valor médio dos carros da concessionária: {media}')
    print()

def gerar_menu():
    print('[0] Cadastrar Carro')
    print('[1] Listar carros')
    print('[2] Buscar carros pelo modelo')
    print('[3] Encontrar o carro mais caro')
    print('[4] Calcular o valor médio dos carros')
    print('[5] Finalizar')
    print()

def main():
    lista = Lista_Dupla()
    
    while True:
        gerar_menu()
        opcao = int(input())
        print()
        
        match opcao:
            case 0:
                cadastrar(lista)
            case 1:
                listar(lista)
            case 2:
                buscar_modelo(lista)
            case 3:
                mais_caro(lista)
            case 4:
                valor_medio(lista)
            case 5:
                print('Obrigado por utilizar o nosso app! \nSaindo...')
                break
            case _:
                print('Opção inválida.')

if __name__ == '__main__':
    main()