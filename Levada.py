class Levada:
    def __init__(self, src, dest, weight):
        """
        Constructs a Levada
        
        Requires:
        src and dst Station
        weight int
        Ensures:
        Levada such that src == self.getSource(), dest == self.getDestination() 
        and weight == self.getWeight() 
        """
        self._src = src
        self._dest = dest
        self._weight = weight

        
    def getSource(self):
        """
        Gets the source Station
        """
        return self._src

    
    def getDestination(self):
        """
        Gets the destination Station
        """
        return self._dest


    def getWeight(self):
        """
        Gets the Levada's weight
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