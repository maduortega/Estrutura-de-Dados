from collections import deque
from random import randint

def comprar():
    lista = []
    
    print('Ações:')
    for i in range(5):
        qtd = randint(10, 200)
        v = randint(10,100)
        
        if i % 2 == 0:
            tp = 1
        else:
            tp = 2
        
        t = tp, qtd, v
        lista.append(t)
        print(t)
    print()
    
    return lista

def vender(acao: list[tuple]) -> float:
    fila = deque()
    montante = 0
    
    for i in acao:
        tipo = i[0]
        if tipo == 1:
            qtd = i[1]
            v = i[2]
            fila.append([qtd, v])
        elif tipo == 2:
            qtd_v = i[1]
            v_venda = i[2]
            
            while qtd_v > 0:
                lote = fila[0]
                if lote[0] <= qtd_v:
                    montante += lote[0] * (v_venda - lote[1])
                    fila.popleft()
                else:
                    montante += qtd_v * (v_venda - lote[1])
                    lote[0] -= qtd_v
                    qtd_v = 0
    return montante

# Programa principal
def main():
    acao = comprar()
    montante = vender(acao)
    print(f'Montante R${montante:.2f}')

if __name__ == '__main__':
    main()