class No:
    def __init__(self, dado):
        self.dado = dado
        self.dir = None
        self.esq = None
        
class Lista_Dupla:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def add_inicio(self, valor): # Valor ou dado, dão no mesmo.
        novo = No(valor) # Criando um nó, chamando o construtor
        
        # Verificar se a lista está vazia (sempre feito da mesma forma)
        
        if self.tamanho == 0: # Ou if self.inicio is None ou self.fim is None
            self.fim = novo # Se é o primeiro valor de uma lista, ele também é o último
        else: # Se já houver um valor, faça isso para add um novo início
            novo.dir = self.inicio
            self.inicio.esq = novo
            self.inicio = novo # Agora o início aponta para o novo início
        
        self.tamanho += 1 # Indifica que agora há ao menos um elemento na lista
        self.inicio = novo # Recebe o primeiro valor da lista, Primeiro end de memória de todos, ou o novo primeiro
        
    def add_final(self, valor):
        novo = No(valor)
        
        if self.tamanho == 0:
            self.inicio = novo # Se for o primeiro valor ele também é o inicio
        else:
            novo.esq = self.fim
            self.fim.dir = novo
        
        self.tamanho += 1
        self.fim = novo
        
    def pesquisar(self, valor) -> No:
        aux = self.inicio
        
        while aux:
            if aux.dado == valor:
                return aux # Retorna o nó (end de memória) onde está o valor encontrado
            aux = aux.dir # Vai andando para o frente até ver se encontra o valor
        return None # 0 para endereço de memória, caso o valor não seja encontrado
    
    def remover(self, valor):
        aux = self.pesquisar(valor) # Antes de remover, temos que pesquisar o valor
        
        if aux is not None: # ou != / if aux
            if self.tamanho == 1: # A lista tem apenas 1 valor
                self.inicio = None
                self.fim = None
            elif aux == self.inicio: # Remove o primeiro elemento
                aux.dir.esq = None # Ao usar o .dir eu chego no próximo elemento, e chegando nele
                # (.esq) eu posso acessar o elemento anterior e remover a conexão
                self.inicio = aux.dir
                aux.dir = None
            elif aux == self.fim: # Remove o último elemento
                aux.esq.dir = None
                self.fim = aux.esq
                aux.esq = None
            else: # Remove um elemento no meio
                aux.esq.dir = aux.dir # O canto direito do anterior recebe o end de memória
                # do bloco seguinte, que está na frente do que vamos remover. Religando a conexão
                aux.dir.esq = aux.esq # Agora o canto esquerdo do próximo recebe o end de memória
                # do bloco anterior, que está atrás do que vamos remover. Religando a conexão
                aux.esq = None
                aux.dir = None
                
            aux = None
            self.tamanho -= 1 # Reduz o tamanho da lista ao remover um valor
    
    def imprimir(self):
        aux = self.inicio
        
        while aux: # Enquanto aux tiver valor / aux != None
            print(aux.dado, end=' ')
            aux = aux.dir # Vai caminhando para a direita

# Programa principal   
     
'''   
lista = Lista_Dupla()

lista.add_inicio(10)
lista.add_inicio(20)
lista.add_inicio(30)

lista.add_final(40)
lista.add_final(50)

print(lista.pesquisar(5))
lista.remover(40)
lista.imprimir() '''