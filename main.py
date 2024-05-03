
class Node(object):
    """
    Class of Nodes
    """

    
    def __init__(self, name):
        """
        Constructs a Node
        
        Requires:
        name is a string
        Ensures:
        node such that name == self.getName()
        """
        self._name = name

        
    def getName(self):
        """
        Gets the name
        """
        return self._name

    
    def __str__(self):
        """
        String representation
        """
        return self._name



class Edge(object):
    """
    Class of Edges
    """
    
    def __init__(self, src, dest):
        """
        Constructs an Edge
        
        Requires:
        src and dst Nodes
        Ensures:
        Edge such that src == self.getSource() and dest == self.getDestination() 
        """
        self._src = src
        self._dest = dest

        
    def getSource(self):
        """
        Gets the source Node
        """
        return self._src

    
    def getDestination(self):
        """
        Gets the destination Node
        """
        return self._dest


    def __str__(self):
        """
        String representation
        """
        return self._src.getName() + '->' + self._dest.getName()



class Digraph(object):
    """
    Class of Directed Graphs
    """


    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children
    def __init__(self):
        """
        Constructs a Directed Graph
        
        Ensures:
        empty Digraph, i.e.
        Digraph such that [] == self.getNodes() and {} == self.getEdges() 
        """
        self._nodes = []
        self._edges = {}

        
    def addNode(self, node):
        """
        Adds a Node
        
        Requires:
        node is Node not in the digraph yet
        Ensures:
        getNodes() == getNodes()@pre.append(node)
        getEdges[node] == [] 
        """
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []

            
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[src].append(dest)

        
    def childrenOf(self, node):
        return self._edges[node]

    
    def hasNode(self, node):
        return node in self._nodes

    
    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'



class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

        

def printPath(path):
    """
    String representation of a path
    
    Requires:
    path a list of nodes
    Ensures:
    string whith nodes' names concatenated by '->'
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


# DFS function as in the book (i.e. without comments):

##def DFS(graph, start, end, path, shortest):
##    path = path + [start]
##    print('Current DFS path:', printPath(path))
##    if start == end:
##        return path
##    for node in graph.childrenOf(start):
##        if node not in path:
##            if shortest == None or len(path) < len(shortest):
##                newPath = DFS(graph, node, end, path, shortest)
##                if newPath != None:
##                    shortest = newPath
##    return shortest
##
##
## # as in the book
##
##def search(graph, start, end):
##    return DFS(graph, start, end, [], None)


# commented (to help students better understand it)

def DFS(graph, start, end, path, shortest):
    """
    Depth first search in a directed graph

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """

    # accumulates; start node entered into the path
    path = path + [start]
    
    # just to keep watching the recursion progressing
    print('Current DFS path:', printPath(path))

    # recursion: base
    # target node is reached (or initially start and end nodes are the same)
    if start == end: 
        return path

    # recursion: step
    # target was not reached and start node is not a leaf (i.e. it has children)
    for node in graph.childrenOf(start):
        
        if node not in path: # to avoid cycles

            # recursive call of DFS function to itself
            # if target was never reached yet before OR
            # this path is still the shortest so far
            if shortest == None or len(path) < len(shortest): 
                newPath = DFS(graph, node, end, path, shortest)
                
                if newPath != None: # if target node was reached
                    shortest = newPath
                    
    # the shortest path found so far after running the for cycle
    return shortest

 
# commented

def search(graph, start, end):
    """
    Wrapper function to initialize DFS function

    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """

    # fourth param: accumulator of nodes (to define path)
    # fifth param: witness: keeps best path found so far
    
    return DFS(graph, start, end, [], None)



def testSP():
    """
    Function to test search in a graph with a specific example
    """
    
    nodes = []
    
    for name in range(7): #Create 7 nodes
        nodes.append(Node(str(name)))
        
    g = Digraph()
    
    for n in nodes:
        g.addNode(n)
        
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[6]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    g.addEdge(Edge(nodes[4],nodes[5]))
    g.addEdge(Edge(nodes[4],nodes[6]))
    g.addEdge(Edge(nodes[6],nodes[5]))
    
    sp = search(g, nodes[0], nodes[5])
    
    print('Shortest path found by DFS:', printPath(sp))


testSP()

    
    
