class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None # 0 para o endereço de memória
        
class ListaSimples:
    def __init__(self):
        self.inicio = None
        
    def inserir_fim(self, dado):
        pass
    
    def inserir_inicio(self, dado):
        novo = No(dado) # Gerando o nó na memória do computador
        if self.inicio is None:
            self.inicio = novo
        else:
            novo.proximo = self.inicio # Antes de ligar o início ligamos o novo ao antigo primeiro
            # Então, o novo primeiro.próximo (end memória do primeiro), recebe o endereço de memmória do último (antigo 1°)
            self.inicio = novo # Já o início é ligado ao novo primeiro depois disso
            
    def imprimir(self):
        aux = self.inicio
        while aux: # Enquanto houver um valor no aux, imprima
            print(aux.dado, end=' -> ') # O dado que está no 1° lugar, a auxiliar tem o acesso
            aux = aux.proximo # Para andarmos para frente, fazemos a aux receber o seu próximo end de memória
            # No caso, ele acessa dentro do nó, o ponteiro para o próximo, indo para o próximo dado + end
    
# Programa principal
lista = ListaSimples()

lista.inserir_inicio(20)
lista.inserir_inicio(25)
lista.inserir_inicio(30)

lista.imprimir()