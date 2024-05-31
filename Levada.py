# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

from codigoOriginal import Edge

class Levada(Edge):
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
        super().__init__(src, dest)
        self._weight = weight


    def getWeight(self):
        """
        Returns the attribute weight.
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