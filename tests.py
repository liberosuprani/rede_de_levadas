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
    
    result = rede.getShortestPaths(s1, s7)
    print(result)
    print("\n-------------------\n")
    result = rede.getShortestPaths(s8, s7)
    print(result)
    print("\n\n\n")
    
    print(s1)
    print(rede)


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
    
    
test1()
#test2()
