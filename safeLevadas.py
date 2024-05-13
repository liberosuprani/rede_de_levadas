import sys
from Network import Network
from Station import Station

# TODO
def readPaths(ficheiro_entrada):
    '''
    '''
    out = []
    with open(ficheiro_entrada, 'r', encoding='utf-8') as arquivo_entrada:
        linhas = arquivo_entrada.readlines()
        
        for linha in linhas:
            # retira a quebra de página caso haja
            if '\n' in linha:
                linha = linha[:-1]
                
            nomes = linha.split(' - ')
            print(linha)
            out.append(nomes)
    return out



# TODO falta fazer toda essa função
def main(levadasNetworkFile, myStationsFile):

    """
    stations = estacoes do levadasNetworkFile
    caminhosAVerificar = caminhos do myStationsFile

    etc123
    """
    wanted_targets_list = readPaths(myStationsFile)
    levadasNetwork = Network()
    levadasNetwork.fromFile(levadasNetworkFile)
        
# main(sys.argv[1], sys.argv[2])
