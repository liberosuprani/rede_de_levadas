# 2023-2024 Programação 2 LTI
# Grupo 54
# 62220 Libero Suprani
# 62239 Lourenço Lima

from copy import deepcopy  
from constants import *
from Station import Station
from Levada import Levada
from codigoOriginal import Graph

class Network(Graph):
    
    def fromFile(self, fileName):
        '''
        Reads the stations from a file whose name is fileName
        
        Requires:
        fileName str
        
        Ensures:
        Data of this network is now according to the data in the file
        '''
        stationsDictionary = {}
        
        with open(fileName, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            lines = lines[1:]
            
            for line in lines:
                # removes all the non important characters (parenthesis, brackets and commas)
                line = line.replace('[', '').replace(']', '').strip()
                line = line.replace('(', '').replace(')', '').strip()
                line = line.split(", ")
                
                # temporary variable for a station
                tempStation = (
                            line[0], 
                            line[1], 
                            [ (line[i], int(line[i+1])) for i in range(2, len(line)-1, 2) ]
                          )
                
                # creates a station with empty children for now, and adds it to the network 
                station = Station(tempStation[0], tempStation[1], [])
                self.addStation(station)
                
                # dictionary key is the ID of a station, 
                # and the value is a tuple (stationObject, listOfChildrenToBeAdded)
                stationId = tempStation[0]
                stationsDictionary[stationId] = (station, tempStation[2])
        
            for currentID in stationsDictionary.keys():
                
                currentStation = stationsDictionary[currentID][0]
                currentChildren = stationsDictionary[currentID][1]
                
                # goes through the list of tuples, with the levadas to be added
                for child in currentChildren:
                    destinationID = child[LEVADA_NODE_INDEX]
                    distance = child[LEVADA_WEIGHT_INDEX]
                    
                    # gets the station Object from its ID key in the dictionary
                    try:
                        destinationStation = stationsDictionary[destinationID][0]
                    except:
                        print(f"There was no info from a station with the ID={destinationID} provided\n") 
                        
                    self.addLevada(Levada(currentStation, destinationStation, distance))
        
        
    def getStations(self):
        """
        Returns the attribute nodes.
        """
        return self._nodes
    
    
    def getLevadas(self):
        """
        Returns the attribute edges.
        """
        return self._edges
    
                 
    def addStation(self, station):
        """
        Adds a station to the network.
        
        Requires:
        station Station
        
        Ensures:
        the addition of station into the network
        """
        Graph.addNode(self, station)

            
    def addLevada(self, levada):
        """
        Adds a Levada
        
        Requires:
        levada is Levada not in the graph yet
        Ensures:
        
        """
        src = levada.getSource()
        dest = levada.getDestination()
        weight = levada.getWeight()
        
        if not(src in self._nodes and dest in self._nodes):
            raise Exception('Stations not in network')
        
        # if this levada does not exist yet, then add it to self._edges
        if (dest, weight) not in self._edges[src]:
            for currentLevada in self._edges[src]:
                # there is already another levada with the same destination station, but different weight
                if currentLevada[LEVADA_NODE_INDEX] == dest and currentLevada[LEVADA_WEIGHT_INDEX] != weight:
                    raise Exception(f"Two levadas with same source station and different weights \
                                    ({Levada(src, dest, currentLevada[LEVADA_WEIGHT_INDEX])}) and ({levada})")
            
            self._edges[src].append((dest, weight))
            self._edges[dest].append((src, weight))

        
    def childrenOf(self, station):
        """
        Gives children of a given station.
        
        Requires:
        station is station already in the network
        Ensures:
        list containing all of the stations that are children of the given station
        """
        return [x[LEVADA_NODE_INDEX] for x in self._edges[station]]
    
    
    def hasStation(self, station=None, stationName=None):
        """
        Returns whether a station exists or not in the network.
        
        Requires:
        station Station (default value = None)
        stationName str (default value = None)
        
        Ensures:
        true if station exists in the network,
        false in case it doesn't
        """
        
        if station != None:
            return Graph.hasNode(station)
        elif stationName != None:
            for currentStation in self._nodes:
                if currentStation.getName() == stationName:
                    return True
            return False
        else:
            raise Exception("No arguments were provided")
    
    
    def getStationFromName(self, stationName):
        """
        Gives a station whose name is provided.
        
        Requires:
        stationName str
        
        Ensures:
        station Station, if station with the given name exists
        False, if it doesn't exist
        """
        for station in self._nodes:
            if station.getName() == stationName:
                return station
        return False
    
    
    def getLevadaBetweenStations(self, station1, station2):
        """
        Gives levada between two given stations
        
        Requires:
        station1, station2 Station
        
        Ensures:
        a tuple, (node1, weightOfTheLevada)  
        """
        if station1 == station2:
            return (0,0)
        if station2 not in self.childrenOf(station1):
            return (0, 0)
        
        for child in self._edges[station1]:
            if child[0] == station2:
                return child
    
    
    def getShortestPaths(self, sourceStation, destinationStation, constraint=3):
        """
        Gives n-shortest paths between two given stations, where n is given (3 by default).
        
        Requires:
        sourceStation, destinationStation Station
        constraint int
        
        Ensures:
        first n-shortest paths, where n is equal to the given constraint 
        """
           
        def isPathElligible(currentPath, allPaths):
            """
            Returns whether a given path is able to be added to the allPaths list 
            (allPaths has to be sorted beforehand)
            
            Requires:
            currentPath tuple (pathList, pathWeight)
            allPaths list (already sorted according to the specification)
            
            Ensures:
            true, if path is "elligible"
            false, in case it's not
            """     
            
            currentPathWeight = currentPath[PATH_WEIGHT_INDEX]
            lastPathWeight = allPaths[-1][PATH_WEIGHT_INDEX]
            
            currentPathList = currentPath[PATH_LIST_INDEX]
            lastPathList = allPaths[-1][PATH_LIST_INDEX]
                  
            if currentPathWeight < lastPathWeight: 
                return True
            
            if currentPathWeight == lastPathWeight:
                if len(currentPathList) > len(lastPathList):
                    return True
                if len(currentPathList) == len(lastPathList):
                    if currentPathList[1].getName() < lastPathList[1].getName():
                        return True
                     
            return False
        
        
        def dfs(currentStation, targetStation, currentPath, pathWeight, allPaths, maxPaths): 
            """
            Gives n-shortest paths between two given stations, where n is given (3 by default).
            
            Requires:
            currentStation, targetStation Station
            currentPath, allPaths list
            pathWeight, maxPaths int
            
            Ensures:
            first n-shortest paths, where n is equal to the given maxPaths 
            """
            currentPath = currentPath + [currentStation]
            
            # if currentPath has at least 2 stations, gets the levada of the previous station with the current station
            # and adds this levada's weight to pathWeight
            if len(currentPath) > 1:
                previousStationLevadas = self._edges[currentPath[-2]]
                currentLevada = None
                for levada in previousStationLevadas:
                    if levada[LEVADA_NODE_INDEX] == currentStation:
                        currentLevada = levada
                pathWeight += currentLevada[LEVADA_WEIGHT_INDEX]
            
            if currentStation == targetStation:
                return (currentPath, pathWeight)
            # if reached a childless station which is not the target station
            elif len(self.childrenOf(currentStation)) == 0:
                return None
            
            for station in self.childrenOf(currentStation):
                if station not in currentPath:  
                    if len(allPaths) < maxPaths or isPathElligible((currentPath, pathWeight), allPaths):      
                        # recursion
                        newPath = (dfs(station, targetStation, currentPath, pathWeight, deepcopy(allPaths), maxPaths))
                        if newPath != None:
                            # if newPath is a tuple (i.e. a path was just found)
                            if isinstance(newPath, tuple):
                                # check whether the amount of paths found until now is lower than constraint or, in case it isn't, 
                                # if currentPath can be added 
                                if len(allPaths) < maxPaths or isPathElligible(newPath, allPaths):
                                    if len(allPaths) == maxPaths: 
                                        allPaths.pop()     
                                    allPaths.append(newPath)
                                    allPaths.sort(key = lambda currentPath: (currentPath[PATH_WEIGHT_INDEX], 
                                                                             -len(currentPath[PATH_LIST_INDEX]), 
                                                                             currentPath[PATH_LIST_INDEX][1].getName()))
                            # if newPath is not a tuple, then it is a list with the last found path already added to it. 
                            # That's why it assigns newPath to the allPaths, so it does not add the last found path to it again.
                            else:
                                allPaths = newPath 
            return allPaths

        results = dfs(sourceStation, destinationStation, [], 0, [], constraint)        
        if len(results) == 0:
            return f"{sourceStation.getName()} and {destinationStation.getName()} do not communicate"
        
        # changes the stations objects for their names to be shown in the list
        results = [ ([station.getName() for station in currentPath[PATH_LIST_INDEX]], 
                     currentPath[PATH_WEIGHT_INDEX]) for currentPath in results ]
        return results


    def __eq__(self, o):
        return (self._nodes == o.getStations() and self._edges == o.getLevadas())

    
    def __str__(self):
        """
        String representation as an adjacency matrix of the network.
        """
        
        finalStr = "Adjacency Matrix:\n/   "
        stations = self._nodes
        
        for station in stations:
            finalStr += f"{station.getId()}   "
        finalStr += "\n"
        
        for row in range(0, len(stations)):
            weightToPrint = 0
            for column in range(-1, len(stations)):
                if column == -1:        
                    finalStr += f"{stations[row].getId()}   "
                else:
                    levada = self.getLevadaBetweenStations(stations[row], stations[column])
                    weightToPrint = levada[1]
                    finalStr += f"{weightToPrint}   "
            finalStr += "\n"
        return finalStr