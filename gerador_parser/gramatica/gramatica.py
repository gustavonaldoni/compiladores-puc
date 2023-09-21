import re

STRING_VAZIA = 'ε'


class Gramatica:
    def __init__(self, nao_terminais: set, terminais: set, producoes: dict, simbolo_inicial: str) -> None:
        self.nao_terminais = nao_terminais
        self.terminais = terminais
        self.producoes = producoes
        self.simbolo_inicial = simbolo_inicial

        self._log_nullable = './log_nullable.txt'

    def mostrar_nao_terminais(self):
        print(f'N = {self.nao_terminais}')

    def mostrar_terminais(self):
        print(f'T = {self.terminais}')

    def mostrar_producoes(self):
        print(self.producoes)

    def mostrar_simbolo_inicial(self):
        print(f'S = {self.simbolo_inicial}')

    def mostrar(self):
        print()
        self.mostrar_nao_terminais()
        self.mostrar_terminais()
        self.mostrar_producoes()
        self.mostrar_simbolo_inicial()
        print()

    def _nullable_escrever(self, simbolo: str, arquivo):
        arquivo.write(f'{simbolo}: ')

        if simbolo in self.terminais:
            arquivo.write('0 ')
            return False

        if STRING_VAZIA in self.producoes[simbolo]:
            arquivo.write('1 ')
            return True

        for derivacao in self.producoes[simbolo]:
            arquivo.write('\n')
            for s in derivacao:
                self._nullable_escrever(s, arquivo)

            arquivo.write('\n')

    def nullable(self, simbolo: str) -> bool:
        with open(self._log_nullable, mode='a+') as arquivo:
            self._nullable_escrever(simbolo, arquivo)

        arquivo = open(self._log_nullable, mode='r')

        conteudo = arquivo.read()
        conteudo = re.sub(r'[\n]{2,}', '\n\n', conteudo)

        indice_primeira_quebra = conteudo.find('\n')
        conteudo = conteudo[indice_primeira_quebra + 1:]

        arquivo.close()

        with open(self._log_nullable, mode='w') as arquivo:
            arquivo.write(conteudo)

        partes = conteudo.split('\n\n')
        print(partes)
        
        for i, parte in enumerate(partes):
            if '0' in parte:
                partes[i] = False
            else:
                partes[i] = True
        
        print(partes)

        if True in partes:
            return True
        
        return False