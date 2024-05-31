# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

import sys
from constants import * 
from Network import Network
from Itinerary import Itinerary
import FileHandling 

def main(levadasNetworkFile, myStationsFile, outputFile):
    """
    Main function.
    
    Requires:
    levadasNetworkFile, myStationsFile, outputFile str
    
    Ensures: 
    the creation of an output file with the name passed in outputFile,
    containing all the wanted paths in myStationsFile, from the levada network
    given in levadasNetworkFile
    """
    # creates a network and fill it with the information in levadasNetworkFile
    levadasNetwork = Network()
    levadasNetwork.fromFile(levadasNetworkFile)
    
    # reads the wanted itineraries from myStationsFile 
    itineraries = FileHandling.readItineraries(myStationsFile)
    
    for currentItinerary in itineraries:
        title = currentItinerary.getTitle()
        sourceStation = title[0]
        destinationStation = title[1]
        
        result = None
        networkHasSource = levadasNetwork.hasStation(stationName=sourceStation)
        networkHasDestination = levadasNetwork.hasStation(stationName=destinationStation)
        
        if sourceStation == destinationStation:
            result = "Same station. 0 minutes."
            
        elif networkHasSource and networkHasDestination:
            sourceNode = levadasNetwork.getStationFromName(sourceStation)
            destNode = levadasNetwork.getStationFromName(destinationStation)
            result = levadasNetwork.getShortestPaths(sourceNode, destNode)  
        else:
            result = ""
            if not networkHasDestination:
                result = f"{destinationStation} out of the network"
                if not networkHasSource:
                    result = f"{sourceStation} and {result}"
            else:
                result = f"{sourceStation} out of the network"
        
        currentItinerary.setAllPaths(result)     
      
    FileHandling.writeItineraries(itineraries, outputFile)
                         

main(sys.argv[1], sys.argv[2], sys.argv[3])
