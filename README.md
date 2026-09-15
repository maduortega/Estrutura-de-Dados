# Estrutura de Dados

Este repositório reúne exercícios, exemplos e implementações desenvolvidos durante os estudos de **Estrutura de Dados**, utilizando a linguagem **Python**.

O material tem como foco a compreensão de como diferentes estruturas organizam, armazenam, acessam e processam dados. A maior parte das atividades foi dedicada à prática com **listas**, **pilhas**, **filas**, **tipos abstratos de dados** e **análise de complexidade**.

Também foram estudados conteúdos relacionados a **árvores** e **grafos**, incluindo árvores binárias de busca, árvores AVL, BFS, DFS e Dijkstra. Esses temas foram trabalhados principalmente por meio da leitura, interpretação e entendimento do funcionamento dos algoritmos, sem a mesma quantidade de exercícios práticos de implementação aplicada às estruturas lineares.

## Conteúdos Abordados

- Tipos abstratos de dados
- Classes e objetos em Python
- Listas simplesmente encadeadas
- Listas duplamente encadeadas
- Pilhas
- Filas
- Uso de `deque`
- Conversão de expressão infixa para pós-fixa
- Análise de complexidade
- Árvores binárias de busca
- Árvores AVL
- Grafos
- Busca em largura, BFS
- Busca em profundidade, DFS
- Caminho mínimo com Dijkstra

## Exercícios em Destaque

| Arquivo | Tema | Principais práticas |
| --- | --- | --- |
| [`Lista Simples/Lista_Simples.py`](<Lista Simples/Lista_Simples.py>) | Lista simplesmente encadeada | Criação de nós, inserção no início e percurso sequencial. |
| [`Lista Dupla/Lista_Dupla.py`](<Lista Dupla/Lista_Dupla.py>) | Lista duplamente encadeada | Inserção, pesquisa, remoção e controle de início, fim e tamanho. |
| [`Pilha/Posfixa.py`](Pilha/Posfixa.py) | Conversão de expressão infixa para pós-fixa | Uso de pilha, prioridade de operadores e processamento de expressões. |
| [`Filas/Exercicio02.py`](Filas/Exercicio02.py) | Simulação com fila | Inserção, consumo, monitoramento e relatório usando `deque`. |
| [`Tipos Abstratos de Dados/Conta.py`](<Tipos Abstratos de Dados/Conta.py>) | Classe Conta | Métodos de depósito, saque, transferência e representação textual. |
| [`Complexidade/Atividade01.py`](Complexidade/Atividade01.py) | Complexidade linear | Percurso de listas e cálculo acumulado com lógica O(n). |
| [`ABB/Abb.py`](ABB/Abb.py) | Árvore binária de busca | Inserção, percurso em ordem, busca e remoção. |
| [`ABB/AVL.py`](ABB/AVL.py) | Árvore AVL | Altura, fator de balanceamento e rotações. |
| [`Grafos/bfs.py`](Grafos/bfs.py) | Busca em largura | Distância, predecessores e ordem de visita. |
| [`Grafos/dfs.py`](Grafos/dfs.py) | Busca em profundidade | Percurso recursivo, predecessores e detecção de ciclos. |
| [`Grafos/dijkstra.py`](Grafos/dijkstra.py) | Caminho mínimo | Fila de prioridade, relaxamento de arestas e reconstrução de caminho. |

## Estrutura do Repositório

```text
.
├── ABB/
├── Atividade Complementar/
├── Atividade_01.py/
├── Atividade_02.py/
├── Complexidade/
├── Filas/
├── Grafos/
├── Lista Dupla/
├── Lista Simples/
├── Pilha/
├── Tipos Abstratos de Dados/
├── LICENSE
└── README.md
```

## Descrição das Pastas

### Tipos Abstratos de Dados

Contém exemplos de classes criadas para representar entidades e comportamentos próprios.

Principais temas:

- Definição de classes
- Métodos construtores
- Atributos de instância
- Métodos de operação
- Sobrescrita de `__str__`
- Modelagem de objetos como conta, item e carrinho

### Lista Simples

Apresenta a base de uma lista simplesmente encadeada.

Principais temas:

- Criação da classe do nó
- Referência para o próximo elemento
- Inserção no início da lista
- Percurso sequencial dos elementos

### Lista Dupla

Reúne exercícios com listas duplamente encadeadas.

Principais temas:

- Nó com referência para o elemento anterior e posterior
- Inserção no início e no final
- Pesquisa de elementos
- Remoção em diferentes posições
- Controle de início, fim e tamanho

### Pilha

Contém exercícios sobre pilhas e o comportamento LIFO, em que o último elemento inserido é o primeiro a ser removido.

Principais temas:

- Inserção e remoção pelo topo
- Uso de `deque`
- Manipulação de expressões
- Conversão de expressão infixa para pós-fixa
- Prioridade de operadores

### Filas

Reúne exercícios sobre filas e o comportamento FIFO, em que o primeiro elemento inserido é o primeiro a ser removido.

Principais temas:

- Inserção no fim da fila
- Remoção no início da fila
- Uso de `popleft`
- Simulações com menus
- Processamento de objetos em ordem de chegada

### Complexidade

Contém atividades voltadas à análise do custo de execução de algoritmos.

Principais temas:

- Noção de crescimento do algoritmo
- Complexidade O(n)
- Percurso de listas
- Cálculo acumulado
- Comparação entre formas de resolver problemas

### ABB

Contém exemplos envolvendo árvores binárias de busca e árvores AVL.

Principais temas:

- Inserção recursiva
- Percurso em ordem
- Remoção de nós
- Busca de menor valor
- Altura da árvore
- Fator de balanceamento
- Rotações em árvores AVL

Árvores foram estudadas com foco no entendimento do código e do funcionamento das operações. O conteúdo não foi aprofundado com uma sequência extensa de exercícios práticos codados do zero.

### Grafos

Contém exemplos de algoritmos clássicos aplicados a grafos.

Principais temas:

- Representação de grafos com dicionários
- Busca em largura, BFS
- Busca em profundidade, DFS
- Detecção de ciclos
- Caminho mínimo com Dijkstra
- Reconstrução de caminhos

Grafos foram estudados principalmente pela leitura, interpretação e compreensão dos algoritmos. O foco foi entender como BFS, DFS e Dijkstra funcionam, sem uma sequência ampla de exercícios práticos de implementação.

## Tecnologias Utilizadas

- **Python**
- **Programação orientada a objetos**
- **Tipos abstratos de dados**
- **Estruturas lineares**
- **Recursividade**
- **Análise de complexidade**
- **Árvores**
- **Grafos**

## Como Executar os Arquivos

Para executar os exercícios, é necessário ter o Python instalado.

No terminal, acesse a pasta do arquivo desejado e execute:

```bash
python nome_do_arquivo.py
```

Exemplo:

```bash
python Posfixa.py
```

Alguns arquivos dependem de classes criadas na mesma pasta, como `Capsula.py`, `Carro.py`, `Paciente.py`, `Produto.py` ou `ListaDupla.py`. Nesses casos, execute o script a partir da própria pasta onde os arquivos estão localizados.

## Observações

As pastas `__pycache__` são geradas automaticamente pelo Python durante a execução dos scripts e não precisam ser alteradas manualmente.

Algumas pastas possuem nomes com `.py`, como `Atividade_01.py/` e `Atividade_02.py/`, mas funcionam como diretórios de organização dos exercícios.

## Objetivo do Repositório

Este repositório tem como objetivo organizar os estudos de **Estrutura de Dados com Python**, registrando a evolução na implementação de estruturas, no raciocínio sobre organização de dados e na compreensão de algoritmos fundamentais para a programação.

## Autoria

Desenvolvido como parte dos estudos de Estrutura de Dados.
