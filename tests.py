from Station import Station
from Network import Network
from Edge import Edge

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
    n.fromFile('ficheiros_entrada/testeLevadas.txt')
    print(n)
    
    
test1()
#test2()
#test3()

