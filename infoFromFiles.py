from Edge import Edge
from Station import Station

#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 143
# 62229 Francisco Gomes 
# 62239 Lourenço Lima



def readStations_Nodes(ficheiro_entrada):
    '''
    reads the nodes/stations
    
    Requires:
    the name of the files
    
    Ensures:
    The list of lists, with the data of each node/station
    '''
    out_lists = []
    out_list_class = []
    
    with open(ficheiro_entrada, 'r', encoding='utf-8') as arquivo_entrada:
        linhas = arquivo_entrada.readlines()
        linhas = linhas[1:]
        
        for linha in linhas:
            # retira a quebra de página caso haja
            if '\n' in linha:
                linha = linha[:-1]
            
            # retira os parenteses retos e normais juntamente com os espaços    
            linha = linha.replace('[', '').replace(']', '').strip()
            linha = linha.replace('(', '').replace(')', '').strip()
            
            id, name = linha.split(', ')[0:2]
            connected = linha.split(', ')[2:]
            
            # faz 2 listas, uma com os caminhos e outra com as distancias
            l1 = connected[::2]
            l2 = connected[1::2]
            
            # junta tudo numa lista de tuplas de 2 
            connected = list(zip(l1, map(int, l2)))
            station = [id, name, connected]
            out_lists.append(station)
            
        # atribui a lista de listas "out_lists" para uma lista de classes "out_list_class"
        for lista in out_lists:
            node = Station(lista[0], lista[1], lista[2])
            out_list_class.append(node)
            
    return out_list_class


# TODO, 
def readPaths_Edges(ficheiro_entrada, list_classes):
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
        
        '''
        # TODO
        # Vai correr a lista de lista com os caminhos
        for lista1 in out:
            
            # Vai comparar cada nome da estação com o nome dos caminhos
            for station in list_classes:
                station = Station()
                if lista1[0] == station.getName() and lista1[1] == station.getName():
                    print('womp womp')
            # TODO, como faço se na lista de caminhos não existir a estação? retorna algo?
        '''
            
    return 0

'''
print(readPaths_Edges('ficheiros_entrada\myStations.txt'))
'''