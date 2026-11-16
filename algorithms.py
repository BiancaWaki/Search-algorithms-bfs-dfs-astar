# Alunos: Gabriel Michel Braucks, Bianca Yuri de Almeida

"""
Data: 18/07/2026

Implementacao dos três algoritmos de busca abaixo:

  * bfs(maze)    -> Busca em Largura   (Breadth-First Search)
  * dfs(maze)    -> Busca em Profundidade (Depth-First Search)
  * astar(maze)  -> Busca A* (A-estrela)
  
"""

from __future__ import annotations

import time
import collections
import heapq
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from maze import Coord, Maze


@dataclass
class SearchResult:
    """Resultado de uma busca, usado pela interface para desenhar a tela."""

    encontrado: bool                 # True se um caminho até o objetivo foi achado
    caminho: List[Coord]             # sequência de células do início ao objetivo (inclusive)
    explorados: List[Coord]          # células visitadas, na ordem em que foram exploradas
    expandidos: int                  # quantidade de células expandidas (nós processados)
    tempo: float                     # tempo de execução em segundos


def reconstruir_caminho(veio_de: Dict[Coord, Coord], inicio: Coord, objetivo: Coord) -> List[Coord]:
    """
    Função utilitária que reconstrói o caminho do `inicio`
    até o `objetivo` a partir do dicionário `veio_de`, onde
    `veio_de[celula]` é a célula anterior no caminho encontrado.
    """
    caminho = [objetivo]
    atual = objetivo
    while atual != inicio:
        atual = veio_de[atual]
        caminho.append(atual)
    caminho.reverse()
    return caminho


def heuristica(a: Coord, b: Coord) -> int:
    """
    Heurística usada pelo A*: distância de Manhattan entre duas células.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# ---------------------------------------------------------------------------
# 1) BUSCA EM LARGURA (BFS)
# ---------------------------------------------------------------------------
def bfs(maze: Maze) -> SearchResult:
    """
    O BFS garante encontrar o caminho mais curto em número de passos
    (todas as arestas têm o mesmo "custo").
    """
    inicio_tempo = time.perf_counter()

    visitados = set()
    explorados = []
    veio_de = {}
    fila = collections.deque([maze.inicio])
    expandidos = 0

    while fila:
        vertice = fila.popleft()

        explorados.append(vertice)
        expandidos += 1
        
        if maze.objetivo == vertice:
            break

        vizinhos = maze.vizinhos(vertice)
        for i in vizinhos:
            if i not in visitados and maze.eh_livre(i):
                visitados.add(i)
                veio_de[i] = vertice
                fila.append(i)

    resultado = SearchResult(
        encontrado=maze.objetivo in explorados,
        caminho=reconstruir_caminho(
            veio_de,
            maze.inicio,
            maze.objetivo
        ),
        explorados=explorados,
        expandidos=expandidos,
        tempo=time.perf_counter() - inicio_tempo
    )

    return resultado


# ---------------------------------------------------------------------------
# 2) BUSCA EM PROFUNDIDADE (DFS)
# ---------------------------------------------------------------------------
def dfs(maze: Maze) -> SearchResult:
    """
    Estrutura de dados sugerida: pilha (lista Python com append/pop),
    processando sempre a última célula inserida (LIFO).

    Diferente do BFS, o DFS NÃO garante o caminho mais curto — ele
    "mergulha" por um caminho até não poder mais avançar antes de
    voltar (backtrack).
    """
    inicio_tempo = time.perf_counter()

    # TODO: implemente aqui a busca em profundidade.

    visitados = set()
    explorados = []
    veio_de = {}
    pilha = collections.deque([maze.inicio])
    expandidos = 0

    while pilha:
        vertice = pilha.pop()

        explorados.append(vertice)
        expandidos += 1
        
        if maze.objetivo == vertice:
            break

        vizinhos = maze.vizinhos(vertice)
        for i in vizinhos:
            if i not in visitados and maze.eh_livre(i):
                visitados.add(i)
                veio_de[i] = vertice
                pilha.append(i)

    resultado = SearchResult(
        encontrado=maze.objetivo in explorados,
        caminho=reconstruir_caminho(
            veio_de,
            maze.inicio,
            maze.objetivo
        ),
        explorados=explorados,
        expandidos=expandidos,
        tempo=time.perf_counter() - inicio_tempo
    )

    return resultado


# ---------------------------------------------------------------------------
# 3) BUSCA A* (A-ESTRELA)
# ---------------------------------------------------------------------------
def astar(maze: Maze) -> SearchResult:
    """
    Estrutura de dados sugerida: fila de prioridade (heapq), ordenada
    por f(n) = g(n) + h(n), onde:
      * g(n) = custo do caminho do início até n (número de passos);
      * h(n) = heuristica(n, maze.objetivo)  (já implementada acima).
    """
    inicio_tempo = time.perf_counter()

    # TODO: implemente aqui a busca A*.

    explorados = []
    veio_de = {}
    g_acumulado = { maze.inicio: 0 }
    contador = 0
    fila = [(heuristica(maze.inicio, maze.objetivo), contador, maze.inicio)]
    fechados = set()

    expandidos = 0

    while fila:
        f_atual, _, vertice = heapq.heappop(fila)

        if vertice in fechados:
            continue

        explorados.append(vertice)
        fechados.add(vertice)
        expandidos += 1
        
        if maze.objetivo == vertice:
            break

        vizinhos = maze.vizinhos(vertice)
        for i in vizinhos:
            if not maze.eh_livre(i):
                continue
            
            custo_tentativo = g_acumulado[vertice] + 1

            if i not in g_acumulado or custo_tentativo < g_acumulado[i]:
                g_acumulado[i] = custo_tentativo
                veio_de[i] = vertice
                f_atual = custo_tentativo + heuristica(i, maze.objetivo)
                contador += 1
                heapq.heappush(fila, (f_atual, contador, i))

    resultado = SearchResult(
        encontrado=maze.objetivo in explorados,
        caminho=reconstruir_caminho(
            veio_de,
            maze.inicio,
            maze.objetivo
        ),
        explorados=explorados,
        expandidos=expandidos,
        tempo=time.perf_counter() - inicio_tempo
    )

    return resultado


# Mapa usado pela interface para associar o texto do dropdown à função
ALGORITMOS = {
    "BFS": bfs,
    "DFS": dfs,
    "A*": astar,
}
