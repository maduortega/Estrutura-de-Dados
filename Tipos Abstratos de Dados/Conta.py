from random import randint

class Conta:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0 # Ao criar uma conta o valor inicial é 0, então não podemos pedir para o user colocá-lo
        self.n_conta = randint(1000, 9999) # O número da conta é gerado automaticamente, não passado pelo user
        
# Programa principal

# Método para depositar um valor na conta
    def depositar(self, valor: float):
        self.saldo += valor
        return self.saldo
   
# Método para sacar um valor da conta     
    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return self.saldo
        else:
            return print('Seu saldo é insuficiente.') # A gente nunca retorna print, só printa direto
        # Deixei só pq ele bizarramente funciona

# Método para transferir um valor da conta   
    def transferir(self, valor: float, conta_dest: 'Conta'):
        if self.saldo >= valor:
            self.sacar(valor) # O mesmo que: self.saldo = self.saldo - valor
            conta_dest.depositar(valor)
            print(f'Transferência de {valor} feita para {conta_dest.titular}, seu saldo atual é de: {self.saldo}')
        else:
            print('Seu saldo é insuficiente.')
        
# Sobrescrever (override)    
    def __str__(self):
        return f'Titular: {self.titular}\n Número: {self.n_conta}\n Saldo: {self.saldo}'
    
# Testes
conta = Conta('Selminininho')
conta2 = Conta('Fafinha')

conta.depositar(7500)
conta.transferir(3500, conta2)

print(f'{conta.titular}, saldo: {conta.saldo} | {conta2.titular}, saldo: {conta2.saldo}')
print()
print(conta) # Agora não printa mais o endereço de memória, graças ao método str