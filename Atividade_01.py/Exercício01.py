# Complexidade O(n³)
# Caso a soma tivesse que ser linear, o código poderia ser O(n²), pois iriamos fazer a soma
# linearmente, logo, seriam necessários, apenas dois laços de repetição

def verificar(lista):
    verificado = False
    
    for i in range(len(lista) - 1):
        soma = 0
        for k in range( len(lista) - 1):
            soma = lista[i] + lista[k + 1]
            for j in range(2, len(lista)):
                if lista[j] == soma:
                    verificado = True
                
    if verificado is True:
        print('Existe um elemento que é a soma de dois anteriores!')
    else:
        print('Nenhum elemento é a soma de dois anteriores.')

def main():
    lista = []
    tamanho = int(input('Informe o tamanho da lista: '))
    for i in range(tamanho):
        n = int(input('Informe os números desejados: '))
        lista.append(n)
        
    verificar(lista)

if __name__ == '__main__':
    main()