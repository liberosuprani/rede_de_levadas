class Station:
    def __init__(self, id, name, neighbors):
        self._id = id
        self._name = name
        self._neighbors = neighbors

    # TODO gets a station from the info in a file
    def fromFile():
        pass


    def getId(self):
        return self._id


    def setId(self, value):
        self._id = value


    def getName(self):
        return self._name


    def setName(self, value):
        self._name = value


    def getNeighbors(self):
        return self._neighbors


    def setNeighbors(self, value):
        self._neighbors = value


    def __str__(self):
        return f"[Id: {self.getId()}, Name: {self.getName()}]"