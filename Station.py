#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 143
# 62220 Libero Suprani 
# 62239 Lourenço Lima

class Station:
    def __init__(self, id, name, children=[]):
        self._id = id
        self._name = name
        
        # children é uma lista com tuplos (nóFilho, distância)
        self._children = children

    # TODO gets a station from the info in a file
    def fromFile(fileName):
        """
        Constructs a station from the info in a file.
        
        Requires:
        fileName str
        Ensures:
        The synchronization of this station's info with the info from the file given
        """
        pass


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