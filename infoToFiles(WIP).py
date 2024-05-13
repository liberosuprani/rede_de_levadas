#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 143
# 62229 Francisco Gomes 
# 62239 Lourenço Lima

from Station import Station
from Edge import Edge
from Network import Network

import infoFromFiles


# TODO, perciso de ver como os testes saiem
def writeFile(horadata, doctors, doctorsHHhMM):
    
    '''
    '''
    
    with open(doctorsHHhMM, 'w', encoding='utf-8') as ficheiro:
        header = f'''Organization:
SmartH
Hour:
{horadata[0]}
Day:
{horadata[1]}
Doctors:'''
        ficheiro.write(header + '\n')
        for doctor in doctors:
           linha = f"{doctor[0]}, {doctor[1]}, {doctor[2]}, {doctor[3]}, {doctor[4]}"
           ficheiro.write(linha + '\n')


# TODO, vê se o teste está certo
# TODO - O que a função vai receber vai ser uma lista de listas ou vai receber classes?
test = [
    [ #primeiras 3 ligações entre o primeiro par de estações
    (['Primeira', 'Terceira', 'Sétima'], 6),
    (['Primeira', 'Oitava', 'Sétima'], 9),
    (['Primeira', 'Segunda', 'Quinta', 'Sétima'], 13)
    ]
    
    
    [ #primeiras 3 ligações entre o primeiro par de estações
    (['Oitava', 'Sétima'], 4), 
    (['Oitava', 'Primeira', 'Terceira', 'Sétima'], 11),
    (['Oitava', 'Primeira', 'Segunda', 'Quinta', 'Sétima'], 18)
    ],
    
    # TODO, em caso da estações não comunicarem:
    # lista vazia
    [
    ]
    
    
    # TODO, em caso de uma das estações do par não tiver no sistema:
    # ()
]