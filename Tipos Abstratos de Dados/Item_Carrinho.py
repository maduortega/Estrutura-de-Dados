''' Alterações realizadas:
    1. substitui a lista no carrinho por um dicionário para melhorar a busca e a atualização.
    2. A busca na lista tem complexidade O(n) enquanto que no dicionário é O(1).
    3. Acrescentei o método str() na classe Item para facilitar a listagem dos itens
    4. Para a remoção de um item no dicionário, podemos utilizar a função del
'''

# classe para definir os dados de cada item
class Item:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def __str__(self):
        return f"Nome = {self.nome}\nPreço = R$ {self.preco}\nQuantidade = {self.quantidade}\n"


# classe para definir os dados e as funcionalidades do carrinho
class Carrinho:
    def __init__(self):
        # troquei por um dicionário para melhorar a busca e facilitar a atualização
        #self.itens = []
        self.itens: dict[str, Item] = {}
        
    # método para adicionar um item no carrinho
    def adicionar_item(self, nome: str, preco: float, quantidade: int):
        if nome in self.itens:
            self.itens[nome].quantidade += quantidade; 
        else:
            self.itens[nome] = Item(nome, preco, quantidade)
        
    # método para calcular e retornar o valor total da compra
    def total(self):
        soma = 0
        for item in self.itens.values():
            soma = soma + item.preco * item.quantidade
        return soma
    
    # método para remover um item (não foi feito durante a aula)
    # utilização de del para dicionários
    def remover_item(self, nome):
        if nome in self.itens:
            del self.itens[nome]

    # método para listar os itens
    def listar_itens(self):
        for item in self.itens.values():
            print(item)
        
# programa principal
carrinho = Carrinho()
carrinho.adicionar_item('lápis', 5.99, 2)
carrinho.adicionar_item('lápis', 5.99, 10)
carrinho.adicionar_item('mouse', 10, 10)
print(carrinho.total())
carrinho.listar_itens()
carrinho.remover_item('lápis')
carrinho.listar_itens()