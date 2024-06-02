# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

from constants import *

class Itinerary:
    def __init__(self, title, route=[]):
        """
        Constructs a Itinerary
        
        Requires:
        title tuple (sourceStationName, destinationStationName)
        route list of tuples (pathList, pathWeight), (default value = [])
        Ensures:
        Itinerary such that title == self.getTitle() and route == self.getAllPaths() 
        """
        self._title = title
        self._route = route
         
    
    def getTitle(self):
        """
        Returns the attribute title.
        """
        return self._title
    
    
    def setTitle(self, title):
        """
        Sets the attribute route.
        """
        self._title = title
    
    
    def getRoute(self):
        """
        Returns the attribute route.
        """
        return self._route
    
    
    def setRoute(self, route):
        """
        Sets the attribute route.
        """
        self._route = route
        
            
    def __str__(self):
        """
        String representation.
        """
        finalStr = f"# {self._title[0]} - {self._title[1]}\n"
        
        if isinstance(self._route, str):
            finalStr += f"{self._route}"
        else:    
            for currentPath in self._route:
                finalStr += f"{currentPath[PATH_WEIGHT_INDEX]}, "

                for station in currentPath[PATH_LIST_INDEX]:
                    finalStr += f"{station}, "
                
                finalStr = finalStr.strip()[:-1] + "\n"
            finalStr = finalStr.strip()
        
        return finalStr