import sys
from Network import Network
from Station import Station

# TODO falta fazer toda essa função 
def main(levadasNetworkFile, myStationsFile):

    """
    stations = estacoes do levadasNetworkFile
    caminhosAVerificar = caminhos do myStationsFile

    etc
    """

    levadasNetwork = Network()
    levadasNetwork.fromFile(levadasNetworkFile)

main(sys.argv[1], sys.argv[2])