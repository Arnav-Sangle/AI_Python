graph = {
    'A': ['C', 'B'],
    'B': ['D', 'E'],
    'D': [],
    'E': [],
    'C': ['G', 'H'],
    'G': [],
    'H': ['I'],
    'I': []
}
# list can store both number and text at same time
visited = []  # List fo nodes


def dfs(key, visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        if node == key:
            print("found")
            exit()
        for neighbour in graph[node]:
            dfs(key, visited, graph, neighbour)


# Driver code
key = input("Enter node to search: ")
print("Performing DFS Goal Test-")
dfs(key, visited, graph, 'A')   # 'A' is source node
