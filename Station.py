class Station:
    def __init__(self, id, name, neighbors):
        self._id = id
        self._name = name
        self._neighbors = neighbors


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

