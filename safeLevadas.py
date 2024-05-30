# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

import sys
from constants import * 
from Network import Network


def readWantedPaths(fileName):
    '''
    Gives the information of the wanted paths from a myStationsFile.
    
    Requires: 
    fileName, a str
    
    Ensures:
    a dictionary, where the keys are tuples with (nameOfSourceStation, nameOfDestinationStation) 
    and the values are empty lists
    '''
    out = {}
    with open(fileName, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        for line in lines:
            names = tuple(line.strip().split(' - '))
            out[names] = []
    return out


def writeFoundPaths(wantedPathsDict, fileName):
    """
    Writes the results from the paths searches into a file.
    
    Requires:
    wantedPathsDict, dict
    fileName, str
    
    Ensures:
    The writing of the content in wantedPathsDict into the file whose name is fileName 
    """
    
    finalStr = ""
    
    for key in wantedPathsDict.keys():
        finalStr += f"# {key[0]} - {key[1]}\n"
        
        # if value of that key is not a list (i.e. a string such as "out of network" or "same station")
        if not isinstance(wantedPathsDict[key], list):
            finalStr += wantedPathsDict[key] + "\n"
        else:
            for path in wantedPathsDict[key]:            
                finalStr += f"{path[PATH_WEIGHT_INDEX]}, "
                
                for station in path[PATH_LIST_INDEX]:
                    finalStr += f"{station}, "
                finalStr = finalStr.rstrip()
                finalStr = finalStr[:-1] + "\n"
                    
    finalStr = finalStr[:-1]    
    with open(fileName, "w", encoding="utf-8") as f:
        f.write(finalStr)



def main(levadasNetworkFile, myStationsFile, outputFileName):
    
    # creates a network and fill it with the information in levadasNetworkFile
    levadasNetwork = Network()
    levadasNetwork.fromFile(levadasNetworkFile)
    
    # reads the wanted paths from myStationsFile 
    wantedPathsDict = readWantedPaths(myStationsFile)
    
    for sourceName, destName in wantedPathsDict.keys():
        result = None
        networkHasSource = levadasNetwork.hasStation(stationName=sourceName)
        networkHasDest = levadasNetwork.hasStation(stationName=destName)
        
        if sourceName == destName:
            result = "Same station. 0 minutes."
            
        elif networkHasSource and networkHasDest:
            sourceNode = levadasNetwork.getStationFromName(sourceName)
            destNode = levadasNetwork.getStationFromName(destName)
            result = levadasNetwork.getShortestPaths(sourceNode, destNode)   
        else:
            result = ""
            if not networkHasDest:
                result = f"{destName} out of the network"
                if not networkHasSource:
                    result = f"{sourceName} and {result}"
            else:
                result = f"{sourceName} out of the network"
        
        wantedPathsDict[(sourceName, destName)] = result    
      
    writeFoundPaths(wantedPathsDict, outputFileName)
                
                
main(sys.argv[1], sys.argv[2], sys.argv[3])
