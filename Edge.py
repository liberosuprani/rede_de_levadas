class Edge:
    def __init__(self, src, dest, weight):
        """
        Constructs an Edge
        
        Requires:
        src and dst Nodes
        weight int
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


    def __eq__(self, o):
        if self.getDestination() == o.getDestination() and self.getSource() == o.getSource() and self.getWeight() == o.getWeight():
            return True
        return False


    def __str__(self):
        """
        String representation
        """
        return f"{self._src.getName()} <-> {self._dest.getName()} ({self.getWeight()})"