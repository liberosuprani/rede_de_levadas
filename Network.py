class Edge:
    def __init__(self, src, dest, weight):
        """
        Constructs an Edge
        
        Requires:
        src and dst Nodes
        Ensures:
        Edge such that src == self.getSource(), dest == self.getDestination() 
        and weight == self.getWeight() 
        """
        self._src = src
        self._dest = dest
        self._weight = weight

        
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


    def getWeight(self):
        """
        Gets the edge's weight
        """
        return self._weight


    def __str__(self):
        """
        String representation
        """
        return self._src.getName() + '->' + self._dest.getName()
    



class Network:
    def __init__(self):
        """
        Constructs a Weighted Graph
        
        Ensures:
        empty graph, i.e.
        graph such that [] == self.getNodes() and {} == self.getEdges() 
        """
        self._nodes = []
        self._edges = {}

        
    def addNode(self, node):
        """
        Adds a Node
        
        Requires:
        node is Node not in the graph yet
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
        weight = edge.getWeight()
        
        if not(src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        
        self._edges[src].append((dest, weight))
        self._edges[dest].append((src, weight))

        
    def childrenOf(self, node):
        return self._edges[node]

    
    def hasNode(self, node):
        return node in self._nodes
                      
    
    #TODO essa função e a outra dentro dela inteiras
    def getShortestPaths(self, sourceNode, destinationNode):
        
        def dfs(graph, start, end, path, shortest, results):
             
            path = path + [start]
            
            if start == end:
                return path
            for node in graph.childrenOf(start):
                if node not in path:
                    
                    #TODO condição para checar se o peso do caminho atual ainda é menor que o dos outros já adicionados no results
                    if shortest == None or : 
                        newPath = dfs(graph, node, end, path, shortest)
                        if newPath != None and sorted(newPath) not in [sorted(x) for x in results]:
                            shortest = newPath
           
            return shortest

        

    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'

        