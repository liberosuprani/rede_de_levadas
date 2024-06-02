# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

from Itinerary import Itinerary
from Network import Network
from collections import UserList

class ItineraryList(UserList):
    def __init__(self, fileName = ""):
        '''
        Constructs a ItineraryList
        
        Requires: 
        fileName, a str (default value = "")
        
        Ensures:
            - ItineraryList with itineraries with their titles 
            (sourceStation, destinationStation), if fileName is provided
            or 
            - an empty list
        '''
        if fileName == "":
            super().__init__()
        else:
            
            itineraries = []
    
            with open(fileName, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                for line in lines:
                    names = tuple(line.strip().split(' - '))
                    itineraries.append(Itinerary(names))
            super().__init__(itineraries)
            
    
    def updateData(self, levadasNetwork):
        """
        Updates the itineraries routes based on their title and the given network
        
        Requires: 
        network Network
        
        Ensures:
        the update of the information regarding the routes in each itinerary 
        """
        for currentItinerary in self.data:
            
            # gets the source and destination station from the itinerary title
            title = currentItinerary.getTitle()
            sourceStation = title[0]
            destinationStation = title[1]
            
            result = None
            networkHasSource = levadasNetwork.hasStation(stationName=sourceStation)
            networkHasDestination = levadasNetwork.hasStation(stationName=destinationStation)
            
            if sourceStation == destinationStation:
                result = "Same station. 0 minutes."
                
            # source and destination both exist in the network
            elif networkHasSource and networkHasDestination:
                sourceNode = levadasNetwork.getStationFromName(sourceStation)
                destNode = levadasNetwork.getStationFromName(destinationStation)
                
                # gets the shortest paths from source to destination
                result = levadasNetwork.getShortestPaths(sourceNode, destNode)  
                
            # at least one of them don't exist in the network
            else:
                result = ""
                if not networkHasDestination:
                    result = f"{destinationStation} out of the network"
                    if not networkHasSource:
                        result = f"{sourceStation} and {result}"
                else:
                    result = f"{sourceStation} out of the network"
            # sets the route in the current itinerary to the result
            currentItinerary.setRoute(result)
    
    
    def toFile(self, fileName):
        """
        Writes the results from the itinerary list into a file.
        
        Requires:
        fileName, str
        
        Ensures:
        The writing of the content in itineraries into the file whose name is fileName 
        """
    
        finalStr = ""
        
        for itinerary in self.data:
            finalStr += f"{str(itinerary)}\n"
        finalStr = finalStr.strip()
                
        with open(fileName, "w", encoding="utf-8") as f:
            f.write(finalStr)          