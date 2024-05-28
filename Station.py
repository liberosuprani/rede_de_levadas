class Station:
    def __init__(self, id, name, children=[]):
        self._id = id
        self._name = name
        
        # children is a list with tuples (childStation, distance)
        self._children = children


    def getId(self):
        return self._id


    def setId(self, value):
        self._id = value


    def getName(self):
        return self._name


    def setName(self, value):
        self._name = value


    def getChildren(self):
        return self._children


    def setChildren(self, value):
        self._children = value


    def __str__(self):
        return f"[Id: {self.getId()}, Name: {self.getName()}]"