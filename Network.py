from copy import deepcopy  
    
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
        return [x[0] for x in self._edges[node]]
    
    
    def hasNode(self, node):
        return node in self._nodes
        
    
    def getShortestPaths(self, sourceNode, destinationNode, constraint=3):
        
        def isWeightEligible(weight, allPaths):
            for path in allPaths:
                if weight < path[1]:
                    return True
            return False
        
        def heaviestPath(allPaths):
            heaviest = None
            for path in allPaths:
                if heaviest == None:
                    heaviest = path
                elif path[1] > heaviest[1]:
                    heaviest = path
            return heaviest                
        
        def dfs(currentNode, targetNode, path, pathWeight, allPaths, maxPaths):
            
            path = path + [currentNode]
            
            # if the current path has at least 2 nodes, get the edge of the previous node with the current node
            # and add this edge's weight to pathWeight
            if len(path) > 1:
                previousNodeEdges = self._edges[path[-2]]
                currentEdge = None
                for edge in previousNodeEdges:
                    if edge[0] == currentNode:
                        currentEdge = edge
                pathWeight += currentEdge[1]
                         
            if currentNode == targetNode:
                return (path, pathWeight)
            
            # if reached a childless node which is not the target node
            elif len(self.childrenOf(currentNode)) == 0:
                return None
            
            for node in self.childrenOf(currentNode):
                if node not in path:
                    
                    if len(allPaths) < maxPaths or (len(allPaths) == maxPaths and isWeightEligible(pathWeight, allPaths)):
                        if len(allPaths) == maxPaths:
                            allPaths.remove(heaviestPath(allPaths))  
                         
                        newPath = (dfs(node, targetNode, path, pathWeight, deepcopy(allPaths), maxPaths))
                        if newPath != None:
                            # if newPath is a tuple (i.e. a path found), append it to the list with all the previous paths
                            if isinstance(newPath, tuple):
                                allPaths.append(newPath)
                            else:
                                allPaths = newPath 
            return allPaths

        results = dfs(sourceNode, destinationNode, [], 0, [], constraint)
        results.sort(key = lambda path: path[1])
        results = [([node.getId() for node in path[0]], path[1]) for path in results]
        return results

    #TODO ver se essa função aqui printa bem levando em conta o grafo ser não direcionado e ponderado
    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'


