from Lista_Dupla import Lista_Dupla
from Carro import Carro   

def main():
    lista = Lista_Dupla()
    n = int(input('Informe a quantidade de carros para registrar: '))
    
    for _ in range(n):
        marca = input('Informe o nome da marca: ')
        modelo = input('Informe o nome do modelo: ')
        valor = float(input('Informe o preço do carro: '))
        print('-' * 60)
        
        lista.add_final(Carro(marca, modelo, valor))
    
    while True: # Permite que o usuário escolha as opções quantas vezes desejar
        n2 = int(input('O que deseja fazer? \n1 - Listar carros | 2 - Buscar carro pelo modelo |\n 3 - Encontrar o carro mais caro | 4 - Valor médio dos carros | 5 - Sair '))
        print('-' * 60)
        
        match n2:
            case 1:
                lista.imprimir() # Imprime tudo que está na lista
                print()
                
            case 2:
                mdl = input('Informe o modelo: ')
                
                aux = lista.inicio
                cont = 0
                while aux: # Enquanto houver dados, procure
                    # Aux.dado --> Objeto carro / .modelo --> Carro.modelo
                    if aux.dado.modelo == mdl: # Se o modelo do carro for o mesmo do input "mdl"
                        print(aux.dado, end='\n') # Printa tudo do carro (deste modelo), \n para não ficar tudo grudado
                        cont = 1
                    aux = aux.dir
                if cont == 0: # Se não for encontrado o modelo, avise.
                    print('Modelo não encontrado.')
                print()
                
            case 3:
                aux = lista.inicio
                maior = 0
                mais_caro = 0
        
                while aux:
                    if aux.dado.valor >= maior: # Compara o preço de um carro com o maior atual
                        maior = aux.dado.valor # Recebe o valor do carro para comparar dnv
                        mais_caro = aux.dado # Recebe o carro inteiro (maior atual)
                    aux = aux.dir
                print(f'Veículo mais caro: {mais_caro}')
                print()
            
            case 4:
                aux = lista.inicio
                soma = 0
                media = 0
        
                while aux:
                    soma += aux.dado.valor # Para cada carro, some o valor dele
                    # O mesmo que fazer uma contagem += 1 e dividir por ela
                    aux = aux.dir # Vai para o próximo carro
                media = soma / lista.tamanho # Divide a soma pelo tamanho (qtd) total de objetos
                print(f'Valor médio dos carros da concessionária: {media}')
                print()
            
            case 5:
                print('Saindo...')
                break
            
            case _: # Se não entrar em qualquer condição acima
                print('Digite uma tecla válida')
            

if __name__ == '__main__':
    main()