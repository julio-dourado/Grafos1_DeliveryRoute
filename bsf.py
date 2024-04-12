#julio aqui vai a bsf do jeitinho que voce falou
from collections import deque, defaultdict

def bfs(graph, start, goal):
    # ja to recebendo um no inicial (start) e um final ne julio fofinho, agora bora visitar todos os vizinhos
    # bora enfilar
    queue = deque([start])
    # listinha de visitados de cria
    visited = {start: None}
    # bora criar a arvore
    tree = defaultdict(list)

    while queue:
        # Pega o nó atual da fila
        current_node = queue.popleft()

        # tem que ver se já é o destino né meu fi
        if current_node == goal:
            break

        # bfs ne papai, bora visitar os vizinhos
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                #agora tem que marcar como visitado
                visited[neighbor] = current_node
                #agora tem que adicionar na arvore
                tree[current_node].append(neighbor)
                #agora tem que adicionar na fila
                queue.append(neighbor)

    # pega a caminhada meu mano xulio
    path = []
    # se o destino foi visitado, bora pegar o caminho (se ele não foi visitado, não tem caminho ne papai, já era)
    #se nn tiver caminho a gente bem que podia mostrar algo pro usuário ne?
    if goal in visited:
        step = goal
        while step is not None:
            path.append(step)
            step = visited[step]
        path.reverse()

    return tree, path

#######################
#Agora a bfs com matriz de adjacencia pro meu mano xulio ficar feliz
def bfsMatrizdef(graph, start, goal):
    queue = deque([start])
    visited = {start: None}
    tree = defaultdict(list)
    n = len(graph)  

    while queue:
        current_node = queue.popleft()
        if current_node == goal:
            break

        for neighbor in range(n):
            if graph[current_node][neighbor] == 1 and neighbor not in visited:
                visited[neighbor] = current_node
                tree[current_node].append(neighbor)
                queue.append(neighbor)

    path = []
    if goal in visited:
        step = goal
        while step is not None:
            path.append(step)
            step = visited[step]
        path.reverse()

    return tree, path
###################################

# grafo aqui pique lista de adjacencia
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
#mas visualmente a parada é mais na pegada da matriz ne?
graphM = [
    [0, 1, 1, 0, 0, 0],  # A tem arestas para B (1) e C (2)
    [0, 0, 0, 1, 1, 0],  # B tem arestas para D (3) e E (4)
    [0, 0, 0, 0, 0, 1],  # C tem uma aresta para F (5)
    [0, 0, 0, 0, 0, 0],  # D não tem arestas
    [0, 0, 0, 0, 0, 1],  # E tem uma aresta para F (5)
    [0, 0, 0, 0, 0, 0]   # F não tem arestas
]
#pega aqui o teste cabuloso, tem com lista e tem com matriz
start_node = 'A' # ou se for pra usar a matriz graphM, seria 0
goal_node = 'F' # ou se for pra usar a matriz graphM, seria 5

#com lista
tree, path = bfs(graph, start_node, goal_node) 
#com matriz
treeM, pathM = bfsMatrizdef(graphM, 0, 5)


print("Árvore de busca:", dict(tree))
print("Menor caminho:", path)

print("Árvore de busca (Matriz):", dict(treeM))
print("Menor caminho (Matriz):", pathM)
