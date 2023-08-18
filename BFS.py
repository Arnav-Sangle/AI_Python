graph = {
            'A':['B', 'C'],
            'B':['D', 'E'],
            'C':['F', 'G'],
            'D':['H', 'I'],
            'H':[],
            'I':[],
            'E':['J', 'K'],
            'J':[],
            'K':[],
            'F':['L', 'M'],
            'L':[],
            'M':[],
            'G':['N', 'O'],
            'N':[],
            'O':[]
        }

#Empty lists
visited = []
queue = []  

def bfs(visited, graph, node):  #function for bfs
    visited.append(node)
    queue.append(node)
    
    while queue:
        m=queue.pop(0)
        print(m, end=" ")
    
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

#Driver code
print("Following is the Depth-First-Search")
srcNode = input("Enter source node: ")
bfs(visited, graph, srcNode)
