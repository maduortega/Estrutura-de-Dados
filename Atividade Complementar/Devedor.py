class Devedor:
    def __init__(self, nome: str, divida: float):
        self.nome = nome
        self.divida = divida
        
     # Ao printar o objeto, não vem o end de memória, e sim essa string, com nome e valor da divida
    def __str__(self):
        return f'Devedor: {self.nome} | Valor da divida: R${self.divida}\n'
        