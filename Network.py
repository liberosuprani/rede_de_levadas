from copy import deepcopy  
from constants import *

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
        
    # TODO gets the network from a given file
    def fromFile(fileName):
        """
        Constructs a network from the info in a file.
        
        Requires:
        fileName str
        Ensures:
        The synchronization of this network's info with the info from the file given
        """
        pass   
     
    
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
        """
        Adds an Edge
        
        Requires:
        edge is Edge not in the graph yet
        Ensures:
        
        """
        src = edge.getSource()
        dest = edge.getDestination()
        weight = edge.getWeight()
        
        if not(src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        
        self._edges[src].append((dest, weight))
        self._edges[dest].append((src, weight))

        
    def childrenOf(self, node):
        """
        Gives children of a given node.
        
        Requires:
        node is Node already in the graph
        Ensures:
        list containing all the children of node
        """
        return [x[EDGE_NODE_INDEX] for x in self._edges[node]]
    
    
    def hasNode(self, node):
        return node in self._nodes
        
    
    def getEdgeBewteenNodes(self, node1, node2):
        """
        Gives edge between two given nodes
        
        Requires:
        node1, node2 Node
        Ensures:
        a tuple, (node1, weightOfTheEdge)  
        """
        if node1 == node2:
            return (0,0)
        if node2 not in self.childrenOf(node1):
            return (0, 0)
        
        for child in self._edges[node1]:
            if child[0] == node2:
                return child
    
    
    def getShortestPaths(self, sourceNode, destinationNode, constraint=3):
        """
        Gives n-shortest paths between two given nodes, where n is given (3 by default).
        
        Requires:
        sourceNode, destinationNode Node
        constraint int
        Ensures:
        first n-shortest paths, where n is equal to the given constraint 
        """
        
        def isWeightEligible(weight, allPaths):
            """
            Returns whether a given weight is lower than any of the paths
            in given.
            
            Requires:
            weight int
            allPaths a list of paths (tuples of (path, weight))
            Ensures:
            True if weight is lower than any of the paths, else returns False
            """
            for path in allPaths:
                if weight < path[PATH_WEIGHT_INDEX]:
                    return True
            return False
        
        
        def heaviestPath(allPaths):
            """
            Gives the heaviest path in a list of paths.
            
            Requires: 
            allPaths a list of paths (tuples of (path, weight))
            Ensures:
            a tuple (path, weight) which is the heaviest path in the allPaths list
            """
            heaviest = None
            for path in allPaths:
                if heaviest == None:
                    heaviest = path
                elif path[PATH_WEIGHT_INDEX] > heaviest[PATH_WEIGHT_INDEX]:
                    heaviest = path
            return heaviest                
        
        
        def dfs(currentNode, targetNode, path, pathWeight, allPaths, maxPaths): 
            """
            Gives n-shortest paths between two given nodes, where n is given (3 by default).
            
            Requires:
            currentNode, targetNode Node
            path, allPaths list
            pathWeight, maxPaths int
            Ensures:
            first n-shortest paths, where n is equal to the given maxPaths 
            """
            path = path + [currentNode]
            
            # if the current path has at least 2 nodes, get the edge of the previous node with the current node
            # and add this edge's weight to pathWeight
            if len(path) > 1:
                previousNodeEdges = self._edges[path[-2]]
                currentEdge = None
                for edge in previousNodeEdges:
                    if edge[EDGE_NODE_INDEX] == currentNode:
                        currentEdge = edge
                pathWeight += currentEdge[EDGE_WEIGHT_INDEX]
                         
            if currentNode == targetNode:
                return (path, pathWeight)
            
            # if reached a childless node which is not the target node
            elif len(self.childrenOf(currentNode)) == 0:
                return None
            
            for node in self.childrenOf(currentNode):
                if node not in path:  
                    if len(allPaths) < maxPaths or (len(allPaths) == maxPaths and isWeightEligible(pathWeight, allPaths)):
                        
                        # if the current path is eligible to be added and the allPaths list is already full,
                        # then remove the heaviest path from allPaths
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

        #TODO ver isso aqui melhor (não sei onde exatamente que é pra guardar a informação de que eles não comunicam)
        results = dfs(sourceNode, destinationNode, [], 0, [], constraint)        
        if len(results) == 0:
            raise Exception(f"{sourceNode.getName()} and {destinationNode.getName()} do not communicate")
        
        results.sort(key = lambda path: path[PATH_WEIGHT_INDEX])
        results = [([node.getName() for node in path[PATH_LIST_INDEX]], path[PATH_WEIGHT_INDEX]) for path in results]
        return results


    def __str__(self):
        finalStr = "Adjacency Matrix:\n/   "
        dictKeys = [k for k in self._edges.keys()]
        nodes = self._nodes
        
        for node in nodes:
            finalStr += f"{node.getId()}   "
        finalStr += "\n"
        
        for row in range(0, len(nodes)):
            weightToPrint = 0
            for column in range(-1, len(nodes)):
                if column == -1:        
                    finalStr += f"{nodes[row].getId()}   "
                else:
                    edge = self.getEdgeBewteenNodes(nodes[row], nodes[column])
                    weightToPrint = edge[1]
                    finalStr += f"{weightToPrint}   "
            finalStr += "\n"
        return finalStr
                    
                


