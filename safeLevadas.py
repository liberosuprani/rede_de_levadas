# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

import sys
from constants import * 
from Network import Network
from ItineraryList import ItineraryList

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
    itineraries = ItineraryList(myStationsFile)    
     
    # updares the itineraries' data based on the network 
    itineraries.updateData(levadasNetwork) 
    itineraries.toFile(outputFile)
                         

main(sys.argv[1], sys.argv[2], sys.argv[3])