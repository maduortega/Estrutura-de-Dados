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
        # Self é a raiz, primeiro elemento da árvore
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
    
    # Método para fazer o percurso em ordem
    def em_ordem(self):
        resultado = []
        self.percurso_em_ordem(self.raiz, resultado) # Vai passando pelo elemento e vai concatenando
        
        return resultado
    
    # Método auxiliar recursivo para fazer o percurso em ordem
    def percurso_em_ordem(self, no, resultado):
        if no is None:
            return
        
        self.percurso_em_ordem(no.esq, resultado)
        resultado.append(no.dado)
        self.percurso_em_ordem(no.dir, resultado)
        
    # Método para remover um elemento da árvore
    def remover(self, dado):
        self.raiz = self.remove(self.raiz, dado)
        
    # Método auxiliar (recursivo) para "remover" (remoção = substituição) um elemento
    def remove(self, no, dado):
        if no is None:
            return None
        
        if dado < no.dado:
            no.esq = self.remove(no.esq, dado)
        elif dado > no.dado:
            no.dir = self.remove(no.dir, dado)
        else:
            # Caso 1 --> O nó não tem filhos (uma folha)
            if no.dir is None and no.esq is None:
                return None # O pai não aponta mais pro filho
            
            # Caso 2 --> O nó tem um filho
            if no.esq is None:
                return no.dir
            if no.dir is None:
                return no.esq
            
            # Caso 3 --> O nó tem dois filhos
            sucessor = self.buscar_menor(no.dir)
            no.dado = sucessor.dado
            no.dir = self.remove(no.dir, sucessor.dado)
        
        return no
            
    def buscar_menor(self, no):
        while no.esq:
            no = no.esq
        return no
                
if __name__ == '__main__':
    arvore = Abb()
    
    arvore.inserir(15)
    arvore.inserir(7)
    arvore.inserir(10)
    arvore.inserir(25)
    arvore.inserir(20)
    arvore.inserir(35)
        
    print(arvore.em_ordem())
    
    arvore.remover(20)
    arvore.remover(7)
    arvore.remover(15)
    
    print(arvore.em_ordem())