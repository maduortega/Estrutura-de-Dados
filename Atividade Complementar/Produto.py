class Produto:
    def __init__(self, nome, qtd, dt_vali):
        self.nome = nome
        self.qtd = qtd
        self.dt_vali = dt_vali
        
    def __str__(self):
        return f'Produto: {self.nome} | Quantidade: {self.qtd} | Data de Validade: {self.dt_vali}\n'
        