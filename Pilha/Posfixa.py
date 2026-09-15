# Pilha é o mesmo que stack
from collections import deque

def prioridade(ch: str) -> int:
    match ch:
        case '(': return 1
        case '+' | '-': return 2 # '|' é o 'or' do match case
        case '*' | '/' | '//' | '%': return 3
        case '^': return 4
        case _: return 0

def converter(expressao: str) -> str:
    pilha = deque()
    posfixa = ''
    
    for ch in expressao:
        if ch != ' ': # Se não for espaço
            if ch in ('+', '-', '*', '/', '//', '%', '^'): # Se o i for alguma dessas expressões na 'lista'
                while pilha and (prioridade(pilha[-1]) >= prioridade(ch)): # -1 acessa o topo da pilha
                    posfixa += pilha.pop() # Remove o último elemento
                pilha.append(ch)
            elif ch == '(':
                pilha.append(ch)
            elif ch == ')':
                while pilha[-1] != '(': # Enquanto o topo da pilha não for um (
                    posfixa += pilha.pop()
                pilha.pop() # Cai fora --> (
            else:
                posfixa += ch
    # Esvazia toda a pilha, caso tenha sobrado algum elemento
    while pilha:
        posfixa += pilha.pop()
        
    return posfixa

# Programa principal
expressao = input('Informe a expressão infixa --> ')
posfixa = converter(expressao)
print(f'Expressão pósfixa --> {posfixa}')