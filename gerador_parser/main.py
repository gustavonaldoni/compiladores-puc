from gramatica.gramatica import Gramatica
from gramatica.gramatica import STRING_VAZIA

if __name__ == '__main__':
    producoes1 = {'S': ['AB', 'BCA'],
                  'A': ['BC', 'aB', 'C'],
                  'B': ['Cb'],
                  'C': [STRING_VAZIA, 'c']}

    gramatica1 = Gramatica(nao_terminais=set({'A', 'B', 'C', 'S'}),
                           terminais=set({'a', 'b', 'c'}),
                           producoes=producoes1,
                           simbolo_inicial='S')

    producoes2 = {'A': ['B', 'a'],
                  'B': ['b', STRING_VAZIA],
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
                  'E': ['y', STRING_VAZIA],
                  'F': ['x', STRING_VAZIA]}

    gramatica4 = Gramatica(nao_terminais=set({'S', 'B', 'D', 'E', 'F'}),
                           terminais=set({'u', 'v', 'w', 'x', 'y', 'z'}),
                           producoes=producoes4,
                           simbolo_inicial='S')

    gramatica1.mostrar()
    print(gramatica1.calcular_nullables())

    gramatica2.mostrar()
    print(gramatica2.calcular_nullables())

    gramatica3.mostrar()
    print(gramatica3.calcular_nullables())

    gramatica4.mostrar()
    print(gramatica4.calcular_nullables())
