# graph = {
#             'A':['B', 'C'],
#             'B':['D', 'E'],
#             'C':['F', 'G'],
#             'D':['H', 'I'],
#             'H':[],
#             'I':[],
#             'E':['J', 'K'],
#             'J':[],
#             'K':[],
#             'F':['L', 'M'],
#             'L':[],
#             'M':[],
#             'G':['N', 'O'],
#             'N':[],
#             'O':[]
#         }

graph = {}
n = int(input("Enter no. of nodes: "))

print("Enter graph (Parent_Node : Child_Node)")
for i in range(n):
    parent = input("Parent Node: ")

    print("Child Nodes: ")
    childList = []
    child = input("\t")
    while child:
        childList.append(child)
        child = input("\t")

    graph[parent] = childList

print(graph)

visited = []
queue = []


def bfs(key, visited, graph, node):
    print("Source node:", node)

    visited.append(node)    # source node appended
    queue.append(node)

    print("Path:", end=" ")
    while queue:
        m = queue.pop(0)    # pop & print visited node
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
bfs(key, visited, graph, 'A')
