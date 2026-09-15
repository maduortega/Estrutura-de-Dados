from collections import deque

def vender(transacao: list[tuple]) -> float:
    fila = deque()
    montante = 0
    
    for t in transacao:
        tipo = t[0]
        if tipo == 'C':
            qtd = t[1]
            v = t[2]
            fila.append([qtd, v]) # Adiciona na fila
        elif tipo == 'V':
            qtd_v = t[1]
            v_venda = t[2]
            
            while qtd_v > 0:
                lote = fila[0]
                if lote[0] <= qtd_v:
                    montante += lote[0] * ( v_venda - lote[1])
                    qtd_v -= lote[0]
                    fila.popleft() # Retira da fila
                else:
                    montante += qtd_v * (v_venda - lote[1])
                    lote[0] -= qtd_v
                    qtd_v = 0
    return montante

# Programa principal
def main():
    transacao = [('C', 100, 20),
                 ('C', 20, 24),
                 ('C', 200, 36),
                 ('V', 150, 30)]

    montante = vender(transacao)
    print(f'Montante R${montante:.2f}')

if __name__ == '__main__':
    main()