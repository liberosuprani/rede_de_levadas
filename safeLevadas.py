import sys
from Network import Network
from Station import Station

# TODO falta fazer toda essa função 
def main(levadasNetworkFile, myStationsFile):
    levadasNetwork = Network()
    levadasNetwork.fromFile(levadasNetworkFile)

main(sys.argv[1], sys.argv[2])