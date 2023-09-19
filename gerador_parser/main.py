from gramatica.gramatica import Gramatica
from gramatica.gramatica import STRING_VAZIA

from gramatica.producao import Producao

if __name__ == '__main__':
    gramatica = Gramatica(nao_terminais=set({'A', 'B', 'C', 'S'}),
                          terminais=set({'a', 'b', 'c'}),
                          producoes=list((Producao('S', list('AB')),
                                          Producao('A', list('a')),
                                          Producao('B', list('bC')),
                                          Producao('C', list('c')))),
                          simbolo_inicial='S')

    gramatica.mostrar()
