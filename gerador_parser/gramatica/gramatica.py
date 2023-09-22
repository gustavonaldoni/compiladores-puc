STRING_VAZIA = 'ε'


class Gramatica:
    def __init__(self, nao_terminais: set, terminais: set, producoes: dict, simbolo_inicial: str) -> None:
        self.nao_terminais = nao_terminais
        self.terminais = terminais
        self.producoes = producoes
        self.simbolo_inicial = simbolo_inicial

        self._nullables = dict()
        self._firsts = dict()
        self._follows = dict()

    def mostrar_nao_terminais(self):
        print(f'N = {self.nao_terminais}')

    def mostrar_terminais(self):
        print(f'T = {self.terminais}')

    def mostrar_producoes(self):
        for lado_esquerdo, producao in self.producoes.items():
            resultado_producao = f'{lado_esquerdo} -> '

            for derivacao in producao:
                resultado_producao += f'{derivacao} | '
            
            resultado_producao = resultado_producao[:-3]
            print(resultado_producao)

    def mostrar_simbolo_inicial(self):
        print(f'S = {self.simbolo_inicial}')

    def mostrar(self):
        print()
        self.mostrar_nao_terminais()
        self.mostrar_terminais()
        self.mostrar_producoes()
        self.mostrar_simbolo_inicial()
        print()

    def producao(self, nao_terminal: str):
        if nao_terminal not in self.nao_terminais:
            raise KeyError(f'{nao_terminal} nao eh simbolo nao terminal.')

        return self.producoes.get(nao_terminal)

    def _definir_nullables_como_falso(self):
        self._nullables = dict()

        for nao_terminal in self.nao_terminais:
            self._nullables.update({nao_terminal: False})

    def _definir_nullable(self, nao_terminal: str, valor: bool):
        if nao_terminal not in self.nao_terminais:
            raise KeyError(f'{nao_terminal} nao eh simbolo nao terminal.')

        self._nullables[nao_terminal] = valor

    def _nullables_atuais(self) -> list[str]:
        return [nao_terminal for nao_terminal in self._nullables.keys() if self._nullables[nao_terminal] == True]

    def _simbolo_e_nullable(self, simbolo: str) -> bool:
        if (simbolo not in self.terminais) and (simbolo not in self.nao_terminais):
            raise KeyError(f'Simbolo {simbolo} nao definido na gramatica')

        if simbolo in self.terminais:
            return False

        if simbolo in self.nao_terminais:
            nullables_atuais = self._nullables_atuais()

            return simbolo in nullables_atuais

        return False

    def calcular_nullables(self) -> dict:
        # Referência: https://mkaul.wordpress.com/2009/12/11/computing-nullable-first-and-follow-sets/
        self._definir_nullables_como_falso()

        # Casos triviais onde X -> STRING_VAZIA
        nullables_triviais = []

        for nao_terminal in self.nao_terminais:
            producao = self.producao(nao_terminal)

            if STRING_VAZIA in producao:
                self._definir_nullable(nao_terminal, True)
                nullables_triviais.append(nao_terminal)

        # Casos onde X -> A e A -> STRING_VAZIA
        for nullable_trivial in nullables_triviais:
            for nao_terminal, producao in self.producoes.items():
                if nullable_trivial in producao:
                    self._definir_nullable(nao_terminal, True)

        # Casos onde X -> ABCDE...
        for nao_terminal, producao in self.producoes.items():
            if nao_terminal not in self._nullables_atuais():
                resultado_nao_terminal = False

                for derivacao in producao:
                    resultado_derivacao = True

                    for simbolo in derivacao:
                        resultado_derivacao = resultado_derivacao and self._simbolo_e_nullable(
                            simbolo)

                    resultado_nao_terminal = resultado_nao_terminal or resultado_derivacao

                self._definir_nullable(nao_terminal, resultado_nao_terminal)

        return self._nullables
