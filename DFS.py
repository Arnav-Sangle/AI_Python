graph = {}      #Empty Dictionary
n = int(input("Enter no. of nodes: "))
print("Enter graph (Parent_Node : Child_Node)")

for i in range(n):
    parent = input("Parent Node: ")
    
    # https://stackoverflow.com/questions/71792347/building-a-list-by-input-python-without-setting-a-number-of-elements#:~:text=if%20you%20were%20to%20take,%3D%22%2C%22)%5D.
    print("Child Nodes: ")
    childList = []  #Empty list
    child=input()
    while child:
        childList.append(child)
        child=input()
      
    graph[parent] = childList

print(graph)

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

visited = set() #set to keep track of visited nodes

def dfs(visited, graph, node): #function for dfs
    if node not in visited:
        print(node),        # , used to print on same line, Doesn't work, use print("text" ,end = " ")
        print(graph[node])
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


#Driver code
print("Following is the Depth-First-Search")
srcNode = input("Enter source node: ")
dfs(visited, graph, srcNode)
