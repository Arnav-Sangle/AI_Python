def aStarAlgo(start_node, stop_node):
    # https://www.geeksforgeeks.org/python-set-method/
    open_set = set(start_node)      # visited
    closed_set = set()              # not visited

    g = {}    # store dist from starting node
    parents = {}    # parents contain an adjacency map of all nodes

    # distance of starting node from itself is zero
    g[start_node] = 0

    # start_node is root node i.e. it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node

    while len(open_set) > 0:            #  len() function returns the number of items in an object
        n = None

        # https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/a-star-search-algorithm/
        # node with lowest f() is found
        for v in open_set:
            if n==None or g[v]+heuristic(v) < g[n]+heuristic(n):    # Total f() = g() + h()     g() = cost start to current       h() = estimate cost current to end
                n = v
        if n==stop_node or Graph_nodes[n]==None:    # condn to stop, when end node is reached
            pass        # https://www.w3schools.com/python/ref_keyword_pass.asp
        else:
            for (m, weight) in get_neighbours(n):
