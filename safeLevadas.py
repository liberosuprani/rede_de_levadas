#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 143
# 62220 Libero Suprani 
# 62239 Lourenço Lima

import sys
from Network import Network
from Station import Station
from Edge import Edge

def calcPaths(dic, paths):
    
    """
    This makes a list of list with and without stations in the network
    
    requires:
    a 'dic' dictonary, the network of stations
    
    ensures:
    2 list of lists, one with the possible paths with the stations out of network (then with 0 and 1) and
    other with the only possible paths only
    """
    
    # Inicializa a lista final que vai armazenar os resultados
    wanted_path_Class = []

    # Itera sobre cada sublista em 'path'
    for sublist2 in paths:
        
        # Inicializa a lista que vai armazenar as classes ou 0/1
        lista_caminho_Classe = ['0OUT_OF_NETWORK', '1OUT_OF_NETWORK']  # Inicialmente 0 e 1 como fallback
        
        # Itera sobre os itens no dicionário 'dic'
        for item in dic.values():
            
            # Verifica se o nome do item corresponde ao primeiro elemento da sublista
            if item.getName() == sublist2[0]:
                lista_caminho_Classe[0] = item  # Substitui o 0 pela classe correspondente
            
            # Verifica se o nome do item corresponde ao segundo elemento da sublista
            elif item.getName() == sublist2[1]:
                lista_caminho_Classe[1] = item  # Substitui o 1 pela classe correspondente
        
        # Adiciona a lista preenchida à lista final
        wanted_path_Class.append(lista_caminho_Classe)
        
        wanted_path_Class_no_numbers = [sublist3 for sublist3 in wanted_path_Class if '0OUT_OF_NETWORK' not in sublist3 and '1OUT_OF_NETWORK' not in sublist3]
    
    return wanted_path_Class, wanted_path_Class_no_numbers


def merge_paths(shortest, paths_with_numbers):
    
    """
    It merges the numbers (the stations that arent in the network) with the shortest path
    
    Requires:
    shortestPaths, a list of lists with the shortest paths
    paths_with_numbers, a list of lists with the paths with numbers
    
    Ensures:
    result, a list of lists, merged with the 2 lists
    """
    
    for i, sublist in enumerate(paths_with_numbers):
        
        if 'BOTH_OUT_OF_NETWORK' in sublist:
            shortest.insert(i, sublist)
        
        if '0OUT_OF_NETWORK' in sublist or '1OUT_OF_NETWORK' in sublist:
            shortest.insert(i, sublist)
    
    def remove_objects_from_list(lst):
        cleaned_list = []  # Lista para armazenar os elementos sem objetos
        for item in lst:
            if isinstance(item, list):
                # Se o item for uma lista, chama a função recursivamente para remover objetos dessa lista
                cleaned_list.append(remove_objects_from_list(item))
            elif not isinstance(item, Station):
                # Se o item não for um objeto da classe Station, adiciona à lista limpa
                cleaned_list.append(item)
        return cleaned_list
    
    return remove_objects_from_list(shortest)



def main(stationsINPUT, wanted_pathsINTPUT, output):

    """
    main function of safeLevadas
    
    requires:
    stationsINPUT, a str with the path of an .txt file
    wanted_pathsINPUT,  a str with the path of an .txt file
    output, a str with the path for the .txt file
    
    ensures:
    an .txt file, with 'output' at his path
    """
    
    n = Network()
    networkDic = n.fromFile(stationsINPUT)    
    wanted_path = Edge.fromFileEdges(wanted_pathsINTPUT)
    
    paths, possiblePaths = calcPaths(networkDic, wanted_path)

    for i, sublist5 in enumerate(paths):
        if '0OUT_OF_NETWORK' in sublist5 and '1OUT_OF_NETWORK' in sublist5:
            out = 'BOTH_OUT_OF_NETWORK'
            paths[i] = [out]

    finalList = []
    for sublist4 in possiblePaths:
        pathList = n.getShortestPaths(sublist4[0], sublist4[1])
        finalList.append(pathList)
    
    merged_final = merge_paths(finalList, paths)
    n.writeFile(wanted_path, merged_final, output)
        
main(sys.argv[1], sys.argv[2], sys.argv[3])

#python safeLevadas.py ficheiros_entrada/stationsTESTE.txt ficheiros_entrada/wantedPathsTESTE.txt ficheiros_saida/outputTESTE.txt
