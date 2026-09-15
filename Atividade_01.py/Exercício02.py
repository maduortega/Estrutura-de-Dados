# Complexidade O(n)

from random import randint
def frequencia(lista):
    novo = {}
    vezes = 0
    mais_rep = 0
    
    for i in range(len(lista)):
        if lista[i] in novo:
            novo[lista[i]] += 1 # Se existir, adicione +1 no valor referente a chave
        else:
            novo[lista[i]] = 1 # Chave = valor     
        
    for chave, valor in novo.items():
        if valor > vezes:
            mais_rep, vezes  = chave, valor
    
    return mais_rep, vezes

def main():
    lista = []
    tamanho = int(input('Informe o tamanho da lista: '))
    cont = 1
    
    while cont <= tamanho:
        n = int(input(f'Informe um número inteiro até {tamanho * 4}: '))
        if n < 0 or n > tamanho*4:
            print('Digite um número inteiro entre 0 e 4')
            continue # Faz com que o laço continue se digitarem um N errado.
        lista.append(n)
        cont += 1
        
    print()
    resul, n_vezes = frequencia(lista)
    print(f'O número que mais repete é: {resul}, que se repete: {n_vezes} vezes')

if __name__ == '__main__':
    main()