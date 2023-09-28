from pprint import pprint

from gramatica.gramatica import Gramatica
from gramatica.gramatica import SIMBOLO_VAZIO, SIMBOLO_EOF


class TabelaParse:
    def __init__(self, gramatica: Gramatica) -> None:
        self.gramatica = gramatica
        self.tabela = dict()

    def _inicializar(self):
        for nao_terminal in self.gramatica.nao_terminais:
            terminais = self.gramatica.terminais.copy()
            terminais.add(SIMBOLO_EOF)

            for terminal in terminais:
                self.tabela.update({(nao_terminal, terminal): list()})

    def _calcular_funcoes(self):
        self.gramatica.calcular_nullables()
        self.gramatica.calcular_firsts()
        self.gramatica.calcular_follows()

    def construir(self):
        # Referência: https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/
        self._inicializar()
        self._calcular_funcoes()

        for nao_terminal, producao in self.gramatica.producoes.items():
            for derivacao in producao:
                if derivacao == SIMBOLO_VAZIO:
                    first = set()
                    e_nullable = True
                else:
                    first = self.gramatica.first(derivacao)
                    e_nullable = self.gramatica.nullable(derivacao)

                for terminal in first:
                    self.tabela[(nao_terminal, terminal)].append(derivacao)

                if e_nullable:
                    follow = self.gramatica.follow(nao_terminal)

                    for terminal in follow:
                        self.tabela[(nao_terminal, terminal)].append(SIMBOLO_VAZIO)

                    if SIMBOLO_EOF in follow:
                        if SIMBOLO_VAZIO in self.tabela[(nao_terminal, SIMBOLO_EOF)]:
                            continue
                        else:
                            self.tabela[(nao_terminal, SIMBOLO_EOF)].append(
                                SIMBOLO_VAZIO
                            )

    def mostrar(self):
        tabela_ainda_nao_construida = len(self.tabela) == 0

        if tabela_ainda_nao_construida:
            self.construir()

        print("Tabela de parse = ", end="")
        pprint(self.tabela)
