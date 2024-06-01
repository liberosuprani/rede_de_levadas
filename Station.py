# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

from codigoOriginal import Node

class Station(Node):
    def __init__(self, id, name, children=[]):
        """
        Constructs a Station
        
        Requires:
        id int 
        name str
        children list of tuples (childStation, distance)
        Ensures:
        Station such that id == self.getId(), name == self.getName() 
        and children == self.getChildren() 
        """
        super().__init__(name)
        self._id = id
        
        # children is a list with tuples (childStation, distance)
        self._children = children


    def getId(self):
        """
        Returns the attribute id.
        """
        return self._id


    def setId(self, value):
        """
        Sets the attribute id.
        """
        self._id = value


    def setName(self, value):
        """
        Sets the attribute name.
        """
        self._name = value


    def getChildren(self):
        """
        Returns the attribute children.
        """
        return self._children


    def setChildren(self, value):
        """
        Sets the attribute children.
        """
        self._children = value


    def __str__(self):
        return f"{self.getId()}, {super().__str__()}"