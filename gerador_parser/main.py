from gramatica.gramatica import Gramatica
from gramatica.gramatica import STRING_VAZIA

if __name__ == '__main__':
    producoes = {'S': ['AB'],
                 'A': ['BC', 'aB', 'C'],
                 'B': ['Cb'],
                 'C': [STRING_VAZIA, 'c']}

    gramatica = Gramatica(nao_terminais=set({'A', 'B', 'C', 'S'}),
                          terminais=set({'a', 'b', 'c'}),
                          producoes=producoes,
                          simbolo_inicial='S')

    gramatica.mostrar()

    print(gramatica.nullable('A'))