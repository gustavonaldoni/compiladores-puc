from gramatica.gramatica import Gramatica
from gramatica.gramatica import SIMBOLO_VAZIO

from analisador_sintatico_preditivo.analisador_sintatico_preditivo import AnalisadorSintaticoPreditivo

if __name__ == '__main__':
    producoes = {'E': ['TX'],
                 'X': ['+TX', SIMBOLO_VAZIO],
                 'T': ['FY'],
                 'Y': ['*FY', SIMBOLO_VAZIO],
                 'F': ['(E)', 'i']}

    gramatica = Gramatica(nao_terminais=set({'E', 'X', 'T', 'Y', 'F'}),
                           terminais=set({'+', '*', '(', ')', 'i'}),
                           producoes=producoes,
                           simbolo_inicial='E')
    
    analisador = AnalisadorSintaticoPreditivo(gramatica)
    
    print(f'Nullables = {gramatica.calcular_nullables()}')
    print(f'Firsts = {gramatica.calcular_firsts()}')
    print(f'Follows = {gramatica.calcular_follows()}')

    analisador.tabela_parse.mostrar()
    analisador.analisar('i*i+i')
