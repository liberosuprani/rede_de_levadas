# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

from constants import *

class Itinerary:
    def __init__(self, title, allPaths=[]):
        """
        Constructs a Itinerary
        
        Requires:
        title tuple (sourceStationName, destinationStationName)
        allPaths list of tuples (pathList, pathWeight), (default value = [])
        Ensures:
        Itinerary such that title == self.getTitle() and allPaths == self.getAllPaths() 
        """
        self._title = title
        self._allPaths = allPaths
        
    
    def getTitle(self):
        """
        Returns the attribute title.
        """
        return self._title
    
    def setTitle(self, title):
        """
        Sets the attribute allPaths.
        """
        self._title = title
    
    
    def getAllPaths(self):
        """
        Returns the attribute allPaths.
        """
        return self._allPaths
    
    def setAllPaths(self, allPaths):
        """
        Sets the attribute allPaths.
        """
        self._allPaths = allPaths
        
        
    def __str__(self):
        """
        String representation.
        """
        finalStr = f"# {self._title[0]} - {self._title[1]}\n"
        
        if isinstance(self._allPaths, str):
            finalStr += f"{self._allPaths}"
        else:    
            for currentPath in self._allPaths:
                finalStr += f"{currentPath[PATH_WEIGHT_INDEX]}, "

                for station in currentPath[PATH_LIST_INDEX]:
                    finalStr += f"{station}, "
                
                finalStr = finalStr.strip()[:-1] + "\n"
            finalStr = finalStr.strip()
        
        return finalStr