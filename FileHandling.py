# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

from Itinerary import Itinerary

def readItineraries(fileName):
    '''
    Gives the information of the wanted itineraries from a myStationsFile.
    
    Requires: 
    fileName, a str
    
    Ensures:
    a list containing the itineraries with their titles (sourceStation, destinationStation)
    '''
    itineraries = []
    
    with open(fileName, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        for line in lines:
            names = tuple(line.strip().split(' - '))
            itineraries.append(Itinerary(names))
    return itineraries


def writeItineraries(itineraries, fileName):
    """
    Writes the results from the paths searches into a file.
    
    Requires:
    itineraries, list of objects of the type Itinerary
    fileName, str
    
    Ensures:
    The writing of the content in itineraries into the file whose name is fileName 
    """
    
    finalStr = ""
    
    for itinerary in itineraries:
        finalStr += f"{str(itinerary)}\n"
    finalStr = finalStr.strip()
            
    with open(fileName, "w", encoding="utf-8") as f:
        f.write(finalStr)