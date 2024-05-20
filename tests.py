from Station import Station
from Network import Network
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

def test1():
    s1 = Station("A", "Primeira", [("B", 1), ("C", 2), ("H", 5)])
    s2 = Station("B", "Segunda", [("A", 1), ("D", 3), ("E", 3)])
    s3 = Station("C", "Terceira", [("A", 2), ("G", 4)])
    s4 = Station("D", "Quarta", [("B", 3), ("F", 4)])
    s5 = Station("E", "Quinta", [("B", 3), ("G", 9)])
    s6 = Station("F", "Sexta", [("D", 4), ("G", 5)])
    s7 = Station("G", "Sétima", [("F", 5), ("E", 9), ("C", 4), ("H", 4)])
    s8 = Station("H", "Oitava", [("A", 5), ("G", 4)])
    
    lista = [s1, s2, s3, s4, s5, s6, s7, s8]
    rede = Network()

    for i in lista:
        rede.addNode(i)
        
    rede.addEdge(Edge(s1, s2, 1))
    rede.addEdge(Edge(s1, s3, 2))
    rede.addEdge(Edge(s2, s4, 3))
    rede.addEdge(Edge(s2, s5, 3))
    rede.addEdge(Edge(s4, s6, 4))
    rede.addEdge(Edge(s5, s7, 9))
    rede.addEdge(Edge(s6, s7, 5))
    rede.addEdge(Edge(s3, s7, 4))
    rede.addEdge(Edge(s1, s8, 5))
    rede.addEdge(Edge(s8, s7, 4))
    
    print("TESTE 1")
    result = rede.getShortestPaths(s1, s7)
    print(result)
    result = rede.getShortestPaths(s8, s7)
    print(result)
    print(s1, end="\n\n")
    print(rede)
    print("--------------------")


def test2():
    s1 = Station("A", "Primeira", [("B", 1), ("C", 2), ("H", 5)])
    s2 = Station("B", "Segunda", [("A", 1), ("D", 3), ("E", 3)])
    s3 = Station("C", "Terceira", [("A", 2), ("G", 4)])
    s4 = Station("D", "Quarta", [("B", 3), ("F", 4)])
    s5 = Station("E", "Quinta", [("B", 3), ("G", 9)])
    s6 = Station("F", "Sexta", [("D", 4), ("G", 5)])
    s7 = Station("G", "Sétima", [("F", 5), ("E", 9), ("C", 4), ("H", 4)])
    s8 = Station("H", "Oitava", [("A", 5), ("G", 4)])
    s9 = Station("I", "Nona", [("J", 4)])
    s10 = Station("J", "Décima", [("I", 4)])
    
    lista = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    rede = Network()

    for i in lista:
        rede.addNode(i)
        
    rede.addEdge(Edge(s1, s2, 1))
    rede.addEdge(Edge(s1, s3, 2))
    rede.addEdge(Edge(s2, s4, 3))
    rede.addEdge(Edge(s2, s5, 3))
    rede.addEdge(Edge(s4, s6, 4))
    rede.addEdge(Edge(s5, s7, 9))
    rede.addEdge(Edge(s6, s7, 5))
    rede.addEdge(Edge(s3, s7, 4))
    rede.addEdge(Edge(s1, s8, 5))
    rede.addEdge(Edge(s8, s7, 4))
    rede.addEdge(Edge(s9, s10, 4))
    
    #result = rede.getShortestPaths(s8, s9)
    #print(result)   
    result = rede.getShortestPaths(s1, s10)
    print(result)  
    
    s1 = None
    
def test3():
    s1 = Station("A", "Primeira")
    s2 = Station("B", "Segunda")
    s3 = Station("C", "Terceira")
    s4 = Station("D", "Quarta")
    s5 = Station("E", "Quinta")
    s6 = Station("F", "Sexta")
    s7 = Station("G", "Sétima")
    s8 = Station("H", "Oitava") 
    
    s1.setChildren(
        [(s2, 1), (s3, 2), (s8, 5)]
    ) 
    s2.setChildren(
        [(s1, 1), (s4, 3), (s5, 3)]
    ) 
    s3.setChildren(
        [(s1, 2), (s7, 4)]
    ) 
    s4.setChildren(
        [(s2, 3), (s6, 4)]
    ) 
    s5.setChildren(
        [(s2, 3), (s7, 9)]
    ) 
    s6.setChildren(
        [(s4, 4), (s7, 5)]
    ) 
    s7.setChildren(
        [(s3, 4), (s5, 9), (s6, 5), (s8, 4)]
    ) 
    s8.setChildren(
        [(s1, 5), (s7, 4)]
    ) 
    
    lista = [s1, s2, s3, s4, s5, s6, s7, s8]
    rede = Network()
    rede.fromStationsList(lista)
    
    print("TESTE 3")
    result = rede.getShortestPaths(s1, s7)
    print(result)
    result = rede.getShortestPaths(s8, s7)
    print(result)
    print(s1, end="\n\n")
    print(rede)
    print("--------------------")



def test4():
    n = Network()
    
    networkDic = n.fromFile('ficheiros_entrada/stationsTESTE.txt')    
    wanted_path = Edge.fromFileEdges('ficheiros_entrada/wantedPathsTESTE.txt')
    
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
    
    print(len(merged_final))
    
    n.writeFile(wanted_path, merged_final, 'ficheiros_saida/TESTE.txt')
    
test4()

#python safeLevadas.py ficheiros_entrada/stationsTESTE.txt ficheiros_entrada/wantedPathsTESTE.txt ficheiros_saida/outputTESTE.txt