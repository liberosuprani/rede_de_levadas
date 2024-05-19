#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 143
# 62220 Libero Suprani 
# 62239 Lourenço Lima

from Station import Station

class Edge:
    def __init__(self, src, dest, weight):
        """
        Constructs an Edge
        
        Requires:
        src and dst Station
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
        Gets the edge's weight
        """
        return self._weight


    def __eq__(self, o):
        if self.getDestination() == o.getDestination() and self.getSource() == o.getSource() and self.getWeight() == o.getWeight():
            return True
        return False
    
    
    def nullEdge(scr, dest):
        """
        It checks if the source and destination station is on the network
        requires:
        a scr and and dest, both Class "Station"
        ensures:
        int 0 if the src doesnt exist
        int 1 if the dest doesnt exist
        """
        
        if scr == None or isinstance(Station, scr):
            return 0
        elif dest == None:
            return 1

    def fromFileEdges(nomeArquivo):
        """
        It reads the myStation.txt file
        Requires:
        a str with the path of myStation.txt file
        Ensures:
        a list of lists with the wanted paths
        """
    
        list_path = []
        with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(' - ')
                list_path.append(partes)
        return list_path

    def __str__(self):
        """
        String representation
        """
        return f"{self._src.getName()} <-> {self._dest.getName()} ({self.getWeight()})"