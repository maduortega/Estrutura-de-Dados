# Classe para definir os dados de cada item
class Item:
    def __init__(self, nome: str, preco: float, qtd: int):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
# Classe para definir os dados e as funcionalidades do carrinho
class Carrinho:
    def __init__(self):
        self.itens = []
    
# Método para adicionar um item no carrinho
    def add(self, nome: str, preco: float, qtd: int):
        self.itens.append({nome: Item(nome, preco, qtd)})
         # {nome: Item(nome, preco, qtd)} | Chave: nome, valor: Objeto (pode por direto no append)
         
         # list = (f'Nome: {nome}, ${preco}, Qtd: {qtd}') para fazer em uma tupla,
         # para desempacotar e usar os valores (tupla dentro do dict) temos que usar zip
        
# Método para calcular e retornar o valor total da compra
    def total(self):
        soma = 0
        for i in self.itens:
            item = i.values()
            soma = soma + item.preco * item.quantidade # ARRUMAR
        return soma

# Programa principal
carrinho = Carrinho()
carrinho.add('Banana', 2.99, 1)
carrinho.total()