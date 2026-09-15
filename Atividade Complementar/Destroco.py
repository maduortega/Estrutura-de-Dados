class Destroco:
    def __init__(self, nome, material, valor):
        self.nome = nome
        self.material = material
        self.valor = valor
        
    def __str__(self):
        return f'Nome do material: {self.nome} | Tipo do material: {self.material} | Valor científico: {self.valor}\n'
        