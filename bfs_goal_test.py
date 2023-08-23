graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'D': [],
    'E': [],
    'C': ['F', 'G'],
    'F': [],
    'G': []
}
# list can store both number and text at same time
visited = []  # List fo nodes
queue = []  # Initialize queue


def bfs(key, visited, graph, node):
    # append source node
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        if m == key:
            break

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver code
key = input("Enter node to search: ")
print("Performing BFS Goal Test-")
bfs(key, visited, graph, 'A')   # 'A' is source node
