#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 143
# 62220 Libero Suprani 
# 62239 Lourenço Lima

from Station import Station
from Edge import Edge
from Network import Network

"""
# TODO, perciso de ver como os testes saiem
def writeFile(lista_caminhos, lista_3_melhores):
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
           
           
        first_path = ""
        second_path = ""
        third_path = ""
        
        
        for lista_caminho in lista_caminho:
            
            with open('myResults.txt', 'w', encoding='utf-8') as file:
                header_path = f'''# {name[0]} - {name[1]}'''
        
            for lista1 in lista_3_melhores:
                for tuple1 in lista1:
                    for name in tuple1:
                        
                        if lista_caminho[0] == name[0] and lista_caminho[1] == name[-1]:
                            file.write(f'''{tuple1[1], }''')

"""             

"""
def escrever_arquivo(test1, test2, nome_arquivo):
    
    with open(nome_arquivo, 'w') as arquivo:
        
        for i in range(len(test1)):
            header_path = f'# {test1[i][0]} - {test1[i][1]}\n'
            arquivo.write(header_path)

            if test2[i][0][0][0] not in test1[i][0] or test2[i][1]:  # Verifica se a sublista não está vazia
                comunicam = False

                for tuplas in test2[i]:
                    path = ', '.join(tuplas[0])
                    path_final = f"{tuplas[1]}, {path}\n"
                    arquivo.write(path_final)
                    comunicam = True

                if not comunicam:
                    arquivo.write(f"{test1[i][0]} and {test1[i][1]} do not communicate\n")
            else:
                arquivo.write(f"{test1[i][0]} and {test1[i][1]} do not communicate\n")

            if test1[i][0] not in [item for sublist in test2[i] for item in sublist[0]]:
                arquivo.write(f"{test1[i][0]} out of the network\n")
            if test1[i][1] not in [item for sublist in test2[i] for item in sublist[0]]:
                arquivo.write(f"{test1[i][1]} out of the network\n")

# Restante do código permanece igual
                
# TODO, vê se o teste está certo
# TODO - O que a função vai receber vai ser uma lista de listas ou vai receber classes?
test2 = [
    [ #primeiras 3 ligações entre o primeiro par de estações
    (['Cedro', 'Queimada'], 76),
    (['Cedro', 'Rabacal', 'Queimada'], 83),
    (['Cedro', 'Ponta do Sol', 'Areeiro', 'Queimada'], 120)
    ],
    
    
    [ #primeiras 3 ligações entre o primeiro par de estações
<<<<<<< Updated upstream:infoToFiles(WIP).py
    (['Queimada', 'Ponta do Sol', 'Pico Ruivo', 'Boavista'], 89),
    ],
    
    # TODO, em caso da estações não comunicarem:
    # lista vazia
    [
    ],
    
    
    # TODO, em caso de uma das estações do par não tiver no sistema:
    # ()
    [ #primeiras 3 ligações entre o primeiro par de estações
    (['Moinho', 'Areeiro', 'Rabacal'], 56), 
    (['Moinho', 'Popias', 'Rabacal'], 56),
    (['Moinho', 'Rabacal'], 18)
    ],
]

test1 = [
    ['Cedro', 'Queimada'],
    ['Ponta do Pargo', 'Calheta'],
    ['Queimada', 'Boavista'],
    ['Areeiro', 'Pico Ruivo'],
    ['Moinho', 'Rabacal']
]

escrever_arquivo(test1, test2, 'ficheiros_entrada/TESTE.txt')
"""

'''
test2 = [
    [
    (['Cedro', 'Queimada'], 76),
    (['Cedro', 'Rabacal', 'Queimada'], 83),
    (['Cedro', 'Ponta do Sol', 'Areeiro', 'Queimada'], 120)
    ],
    
    [
    (['Queimada', 'Ponta do Sol', 'Pico Ruivo', 'Boavista'], 89),
    ],
    
    [
    ],

    [ 
    (['Moinho', 'Areeiro', 'Rabacal'], 56), 
    (['Moinho', 'Popias', 'Rabacal'], 56),
    (['Moinho', 'Rabacal'], 18)
    ]
]

test1 = [
    ['Cedro', 'Queimada'],
    ['Ponta do Pargo', 'Calheta'],
    ['Queimada', 'Boavista'],
    ['Areeiro', 'Pico Ruivo'],
    ['Moinho', 'Rabacal']
]
'''




def escrever_arquivo(lista_estacao, lista_3_melhores, nome_arquivo):
    
    with open(nome_arquivo, 'w') as arquivo:
        
        
        for par_estacoes, sublistas in zip(lista_estacao, lista_3_melhores):
            
            arquivo.write(f'# {par_estacoes[0]} - {par_estacoes[1]}\n')
            
            # se não houver nada na lista:
            if not sublistas:
                arquivo.write(f"{par_estacoes[0]} and {par_estacoes[1]} do not communicate\n")    
            else:
                arquivo.write(f"comunica!\n")
                
                '''
                for tupla in sublistas:
                    if par_estacoes[0] in tupla[0] and par_estacoes[1] in tupla[0]:
                            str_paths =', '.join(tupla[0])
                            arquivo.write(f'{tupla[1]}, {str_paths}\n')
                            
                    elif par_estacoes[0] not in tupla[0] and par_estacoes[1] not in tupla[0]:
                        if par_estacoes[0] not in tupla[0]:
                            arquivo.write(f"{par_estacoes[0]} is out of the network\n")
                        else:
                            arquivo.write(f"{par_estacoes[1]} is out of the network\n")
                '''


    
    
    
    '''
    with open(nome_arquivo, 'w') as arquivo:
        for list in test1:
            arquivo.write(f'# {list[0]} - {list[1]}\n')
            
            for sublist in test2:
                
                
                if len(sublist) == 0:
                    arquivo.write(f"{list[0]} and {list[1]} do not communicate\n")
                else:
                    arquivo.write("comunica!\n")
    '''
    
'''    
                else:
                    
                    for tupla in sublist:
                        #for sublista_caminho in tupla[:-1]:
                        
                        if list[0] in tupla[0] and list[1] in tupla[0]:
                            str_paths =', '.join(tupla[0])
                            arquivo.write(f'{tupla[1]}, {str_paths}\n')
                            
                        elif list[0] not in tupla[0] and list[1] not in tupla[0]:
                            if list[0] not in tupla[0]:
                                arquivo.write(f"{list[0]} is out of the network\n")
                            else:
                                arquivo.write(f"{list[1]} is out of the network\n")
'''

# TODO, vê se o teste está certo
# TODO - O que a função vai receber vai ser uma lista de listas ou vai receber classes?
test2 = [
    [ #primeiras 3 ligações entre o primeiro par de estações
    (['Cedro', 'Queimada'], 76),
    (['Cedro', 'Rabacal', 'Queimada'], 83),
    (['Cedro', 'Ponta do Sol', 'Areeiro', 'Queimada'], 120)
    ],
    
    
    [ #primeiras 3 ligações entre o primeiro par de estações
    (['Queimada', 'Ponta do Sol', 'Pico Ruivo', 'Boavista'], 89),
    ],
    
    # TODO, em caso da estações não comunicarem:
    # lista vazia
    [
    ],
    
    
    # TODO, em caso de uma das estações do par não tiver no sistema:
    # ()
    [ #primeiras 3 ligações entre o primeiro par de estações
    (['Moinho', 'Areeiro', 'Rabacal'], 56), 
    (['Moinho', 'Popias', 'Rabacal'], 56),
    (['Moinho', 'Rabacal'], 18)
    ]
]



test1 = [
    ['Cedro', 'Queimada'],
    ['Ponta do Pargo', 'Calheta'],
    ['Queimada', 'Boavista'],
    ['Areeiro', 'Pico Ruivo'],
    ['Moinho', 'Rabacal']
]



'''
test2_1 = [
    [
    (['Primeira', 'Terceira', 'Sétima'], 6),
    (['Primeira', 'Oitava', 'Sétima'], 9),
    (['Primeira', 'Segunda', 'Quinta', 'Sétima'], 13)
    ],
    
    [   
    ],
    
    [
    (['Oitava', 'Sétima'], 4),
    (['Oitava', 'Primeira', 'Terceira', 'Sétima'], 11),
    (['Oitava', 'Primeira', 'Segunda', 'Quinta', 'Sétima'], 18)
    ]
]
'''

'''
test1_1 = [
    ['Primeira', 'Sétima'],
    ['Primeira', 'Nona'],
    ['Segunda', 'Nona'],
    ['Oitava', 'Sétima']
]
'''

escrever_arquivo(test1, test2, 'ficheiros_entrada/TESTE.txt')





=======
    (['Oitava', 'Sétima'], 4), 
    (['Oitava', 'Primeira', 'Terceira', 'Sétima'], 11),
    (['Oitava', 'Primeira', 'Segunda', 'Quinta', 'Sétima'], 18)
    ]
    
    # TODO, em caso da estações não comunicarem:
    # (escreve aqui no teste o resultado pra poder fazer o if na função)
    
    
    # TODO, em caso de uma das estações do par não tiver no sistema:
    # (escreve aqui no teste o resultado pra poder fazer o if na função)
]
>>>>>>> Stashed changes:infoToFiles.py
