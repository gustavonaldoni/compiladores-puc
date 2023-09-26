from gramatica.gramatica import Gramatica
from gramatica.gramatica import SIMBOLO_VAZIO

from tabela_parse.tabela_parse import TabelaParse

if __name__ == '__main__':
    producoes1 = {'S': ['AB', 'BCA'],
                  'A': ['BC', 'aB', 'C'],
                  'B': ['Cb'],
                  'C': [SIMBOLO_VAZIO, 'c']}

    gramatica1 = Gramatica(nao_terminais=set({'A', 'B', 'C', 'S'}),
                           terminais=set({'a', 'b', 'c'}),
                           producoes=producoes1,
                           simbolo_inicial='S')

    producoes2 = {'A': ['B', 'a'],
                  'B': ['b', SIMBOLO_VAZIO],
                  'C': ['c', 'ABC']}

    gramatica2 = Gramatica(nao_terminais=set({'A', 'B', 'C'}),
                           terminais=set({'a', 'b', 'c'}),
                           producoes=producoes2,
                           simbolo_inicial='A')
    
    producoes3 = {'S': ['cABc'],
                  'A': ['aAa', 'c'],
                  'B': ['bBb', 'c']}

    gramatica3 = Gramatica(nao_terminais=set({'S', 'A', 'B'}),
                           terminais=set({'a', 'b', 'c'}),
                           producoes=producoes3,
                           simbolo_inicial='S')
    
    producoes4 = {'S': ['uBDz'],
                  'B': ['Bv', 'w'],
                  'D': ['EF'],
                  'E': ['y', SIMBOLO_VAZIO],
                  'F': ['x', SIMBOLO_VAZIO]}

    gramatica4 = Gramatica(nao_terminais=set({'S', 'B', 'D', 'E', 'F'}),
                           terminais=set({'u', 'v', 'w', 'x', 'y', 'z'}),
                           producoes=producoes4,
                           simbolo_inicial='S')
    
    num = ('N', 'num')

    producoes5 = {'S': ['E'],
                  'E': ['T+E', 'T'],
                  'T': [f'{num[0]}*T', num[0]]}

    gramatica5 = Gramatica(nao_terminais=set({'S', 'E', 'T'}),
                           terminais=set({num[0], '+', '*'}),
                           producoes=producoes5,
                           simbolo_inicial='S')

    DS = ('1', 'DS')
    DS_Linha = ('2', 'DS_Linha')

    producoes6 = {DS[0]: [f'D{DS_Linha[0]}'],
                  DS_Linha[0] : [f';{DS[0]}', SIMBOLO_VAZIO],
                  'D' : 's'}

    gramatica6 = Gramatica(nao_terminais=set({DS[0], DS_Linha[0], 'D'}),
                           terminais=set({'s', ';'}),
                           producoes=producoes6,
                           simbolo_inicial=DS[0])
    
    tabela_parse_6 = TabelaParse(gramatica6)

    producoes7 = {'S': ['(S)S', SIMBOLO_VAZIO]}

    gramatica7 = Gramatica(nao_terminais=set({'S'}),
                           terminais=set({'(', ')'}),
                           producoes=producoes7,
                           simbolo_inicial='S')
    
    tabela_parse_7 = TabelaParse(gramatica7)
    
    gramatica1.mostrar()
    print(f'Nullables = {gramatica1.calcular_nullables()}')
    print('Firsts = ', gramatica1.calcular_firsts())
    print('Follows = ', gramatica1.calcular_follows())

    gramatica2.mostrar()
    print(f'Nullables = {gramatica2.calcular_nullables()}')
    print('Firsts = ', gramatica2.calcular_firsts())
    print('Follows = ', gramatica2.calcular_follows())

    gramatica3.mostrar()
    print(f'Nullables = {gramatica3.calcular_nullables()}')
    print('Firsts = ', gramatica3.calcular_firsts())
    print('Follows = ', gramatica3.calcular_follows())

    gramatica4.mostrar()
    print(f'Nullables = {gramatica4.calcular_nullables()}')
    print('Firsts = ', gramatica4.calcular_firsts())
    print('Follows = ', gramatica4.calcular_follows())

    gramatica5.mostrar()
    print(f'Nullables = {gramatica5.calcular_nullables()}')
    print('Firsts = ', gramatica5.calcular_firsts())
    print('Follows = ', gramatica5.calcular_follows())

    gramatica6.mostrar()
    print(f'Nullables = {gramatica6.calcular_nullables()}')
    print('Firsts = ', gramatica6.calcular_firsts())
    print('Follows = ', gramatica6.calcular_follows())

    tabela_parse_6.construir()
    tabela_parse_6.mostrar()

    gramatica7.mostrar()
    print(f'Nullables = {gramatica7.calcular_nullables()}')
    print('Firsts = ', gramatica7.calcular_firsts())
    print('Follows = ', gramatica7.calcular_follows())

    tabela_parse_7.construir()
    tabela_parse_7.mostrar()
