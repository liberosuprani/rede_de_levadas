import sys
from Network import Network

<<<<<<< HEAD

def readPaths(fileName):
    '''
    '''
    out = {}
    with open(fileName, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        for line in lines:
            names = tuple(line.strip().split(' - '))
            out[names] = []
    return out
print(readPaths('ficheiros_entrada/myStations.txt'))

def writePaths(dictionary, fileName):
    #TODO talvez dê pra melhorar esse código aqui mas eu tô com sono e depois e vejo, são 2h da manhã
    
    finalStr = ""
    
    for key in dictionary.keys():
        finalStr += f"# {key[0]} - {key[1]}\n"
        if not isinstance(dictionary[key], list):
            finalStr += dictionary[key] + "\n"
        else:
            for path in dictionary[key]:            
                    finalStr += f"{path[1]}, "
                    for station in path[0]:
                        finalStr += f"{station}, "
                    finalStr = finalStr.rstrip()
                    finalStr = finalStr[:-1] + "\n"
                    
    finalStr = finalStr[:-1]    
    print(finalStr)
    with open(fileName, "w", encoding="utf-8") as f:
        f.write(finalStr)

=======
# TODO falta fazer toda essa função 
def main(levadasNetworkFile, myStationsFile):
>>>>>>> parent of 4460622 (stationsFromFile feito)

def main(levadasNetworkFile, myStationsFile, outputFileName):
    """
    stations = estacoes do levadasNetworkFile
    caminhosAVerificar = caminhos do myStationsFile

    etc123
    """
<<<<<<< HEAD
    
    levadasNetwork = Network()
    levadasNetwork.fromFile(levadasNetworkFile)
    
    wantedPathsDict = readPaths(myStationsFile)
    
    for sourceName, destName in wantedPathsDict.keys():
        result = None
        networkHasSource = levadasNetwork.hasNode(nodeName=sourceName)
        networkHasDest = levadasNetwork.hasNode(nodeName=destName)
        
        if networkHasSource and networkHasDest:
            sourceNode = levadasNetwork.getNodeFromName(sourceName)
            destNode = levadasNetwork.getNodeFromName(destName)
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
      
    writePaths(wantedPathsDict, outputFileName)
        
main("ficheiros_entrada/testeLevadas.txt", "ficheiros_entrada/testeMyStations.txt", "myResults.txt")         
#main(sys.argv[1], sys.argv[2], sys.argv[3])

"""
PEEEEEEEEEEEEEEEEEEEEEEENNNNNNNNNNNNNNNIIIIIIIIIISSSSSSSSSS
"""
=======

    levadasNetwork = Network()
    levadasNetwork.fromFile(levadasNetworkFile)

main(sys.argv[1], sys.argv[2])
>>>>>>> parent of 4460622 (stationsFromFile feito)
