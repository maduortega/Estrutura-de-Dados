from Lista_Dupla import Lista_Dupla

class Carro:
    def __init__(self, marca: str, modelo: str, valor: float):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        
    # Ao printar o objeto, não vem o end de memória, e sim essa string, com marca modelo e valor
    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Preço: R${self.valor}\n'
        
# Programa principal
''' lista = Lista_Dupla()
lista.add_final(Carro('Chevrolet', 'Impala 67', 320000))
lista.add_final(Carro('Camaro', 'z28', 270000))

lista.imprimir() '''