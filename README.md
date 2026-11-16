# Maze Solver — Comparação de Algoritmos de Busca

Projeto para o trabalho de Inteligência Artificial:
implementação e comparação dos algoritmos **BFS**, **DFS** e **A\*** na
resolução de um labirinto.

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

Uma janela deve abrir com:

- um **tabuleiro** (labirinto gerado aleatoriamente), com o ponto de
  início em **verde** (canto superior esquerdo) e o objetivo em
  **vermelho/rosa**; obstáculos em **preto** e células livres em cinza;
- um **dropdown** para escolher o algoritmo: `BFS`, `DFS` ou `A*`;
- um botão **Executar**, que roda o algoritmo escolhido sobre o
  labirinto atual;
- um botão **Novo Labirinto**, que gera um novo tabuleiro aleatório;
- uma linha de **estatísticas** (tamanho do caminho, nós expandidos e
  tempo de execução) e uma **legenda** de cores.

## Estrutura do projeto

```
maze_solver/
├── main.py         # Ponto de entrada: janela, loop principal, eventos (PRONTO)
├── ui.py           # Cores, botão, dropdown e desenho do tabuleiro (PRONTO)
├── maze.py         # Representação e geração do labirinto (PRONTO)
├── algorithms.py   # Implementação BFS, DFS e A* >>>
└── requirements.txt
```

## Requisitos

- Python 3.10+
- pygame (`pip install pygame`)
