class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        
class Abb:
    def __init__(self):
        # Única coisa que temos da árvore
        self.raiz = None
        
    # Método para inserir um dado na árvore binária de busca
    def inserir(self, dado):
        dado = dado.lower() # Converte tudo para minúsculo
        self.raiz = self.insere(self.raiz, dado) # End. Primeiro elemento, dado a ser inserido
        
    # Método recursivo para inserir um dado na árvore
    def insere(self, no, dado): # Nó pode ser a raiz ou não
        if no is None:
            return No(dado)
        
        if dado < no.dado:
            no.esq = self.insere(no.esq, dado)
        elif dado > no.dado:
            no.dir = self.insere(no.dir, dado)
            
        return no
    
    # Método para buscar os nomes que começam com um determinado prefixo
    def buscar(self, prefixo):
        prefixo = prefixo.lower()
        resultado = []
        self.busca(self.raiz, prefixo, resultado)
        
        return resultado
    
    # Método recursivo para busca
    def busca(self, no, prefixo, resultado):
        if no is None:
            return
        
        if prefixo < no.dado:
            self.busca(no.esq, prefixo, resultado)
            
        if no.dado.startswith(prefixo):
            resultado.append(no.dado)
            
        # Ou + chr(127) --> Número ascii do botão delete, maior caractere da tabela ascii
        # Para garantir que ele busque valores na direita se ele achar na esquerda primeiro
        # pois, ao achar na esquerda ele não via os da direita, o que é um erro.
        if (prefixo + '}') > no.dado:
            self.busca(no.dir, prefixo, resultado)
        
# Programa principal
if __name__ == '__main__':
    abb = Abb()
    
    usuarios = ["mariana", "marcos", "mario", "ana", "marina", "bruna", "marcelo"]
    
    for user in usuarios:
        abb.inserir(user)
    
    print(abb.buscar('mar'))