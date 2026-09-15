class No:
    def __init__(self, timestamp, preco):
        self.timestamp = timestamp
        self.preco = preco
        self.esq = None
        self.dir = None
        
class Abb:
    def __init__(self):
        # Única coisa que temos da árvore
        self.raiz = None
        
    # Método para inserir um dado na árvore binária de busca
    def inserir(self, dado):
        dado, valor = dado
        self.raiz = self.insere(self.raiz, dado, valor) # End. Primeiro elemento, dado a ser inserido
        
    # Método recursivo para inserir um dado na árvore
    def insere(self, no, dado, valor): # Nó pode ser a raiz ou não
        if no is None:
            return No(dado, valor)
        
        if dado < no.timestamp:
            no.esq = self.insere(no.esq, dado, valor)
        elif dado > no.timestamp:
            no.dir = self.insere(no.dir, dado, valor)
            
        return no
    
    # Método para retornar o preço exato para o timestamp informado, ou None
    def buscar(self, dado):
        dado
        resultado = []
        self.busca(self.raiz, dado, resultado)
        
        return resultado
    
    # Método recursivo para busca
    def busca(self, no, dado, resultado):
        if no is None:
            return
        
        if dado < no.timestamp:
            self.busca(no.esq, dado, resultado)
            
        if dado == no.timestamp:
            resultado.append(no.preco)
            
        # Ou + chr(127) --> Número ascii do botão delete, maior caractere da tabela ascii
        # Para garantir que ele busque valores na direita se ele achar na esquerda primeiro
        # pois, ao achar na esquerda ele não via os da direita, o que é um erro.
        if dado > no.timestamp:
            self.busca(no.dir, dado, resultado)
            
     # Método para fazer o percurso em ordem
    def em_ordem(self, inicio, fim):
        resultado = []
        self.percurso_em_ordem(self.raiz, inicio, fim, resultado) # Vai passando pelo elemento e vai concatenando
        
        return resultado
    
    # Método auxiliar recursivo para fazer o percurso em ordem
    def percurso_em_ordem(self, no, inicio, fim, resultado):
        if no is None:
            return
        
        if no.timestamp < inicio: # Está na direita, descartamos a esquerda
            self.percurso_em_ordem(no.dir, inicio, fim, resultado)
            
        if no.timestamp >= inicio and no.timestamp <= fim: # Está dentro do intervalo (achou)
# Se estiver no intervalo, chamamos a recursividade pro código continuar funcionando. Se não 
# fizermos isso, ele entra nesse if, "appenda" e para. Logo, temos que chamar o em ordem --> E R D

            self.percurso_em_ordem(no.esq, inicio, fim, resultado) # Esquerda
            resultado.append(no.timestamp) # Raiz
            self.percurso_em_ordem(no.dir, inicio, fim, resultado) # Direita
            
        if no.timestamp > fim: # Está na esquerda, descartamos a direita
            self.percurso_em_ordem(no.esq, inicio, fim, resultado)
            
# Programa principal
if __name__ == '__main__':
    abb = Abb()
    
    cotacoes = [
        (1000, 62400.0), # dia 1, 00:00
        (1100, 63100.5), # dia 1, 00:10
        (1200, 61800.0), # dia 1, 00:20
        (1300, 64500.0), # dia 1, 00:30
        (1400, 65200.0), # dia 1, 00:40
        (1500, 63900.0), # dia 1, 00:50
    ]
    
    for cot in cotacoes:
        abb.inserir(cot)
    
    print('Preço para este timestamp:')
    print(abb.buscar(1200))
    print()
    
    print('Timestamp dentro do intervalo:')
    # range(inicio, fim)
    print(abb.em_ordem(1100, 1300))