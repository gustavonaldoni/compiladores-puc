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

    def nullable(self, string: str) -> bool:
        resultado = True
        nullables_nao_foram_calculados = len(self._nullables) == 0

        if nullables_nao_foram_calculados:
            self.calcular_nullables()

        for simbolo in string:
            if (simbolo not in self.terminais) and (simbolo not in self.nao_terminais):
                raise KeyError(f'Simbolo {simbolo} nao definido na gramatica')
            
            if simbolo in self.terminais:
                return False

            if simbolo in self.nao_terminais:
                resultado = resultado and self._nullables[simbolo]

        return resultado

    def _definir_firsts(self):
        self._firsts = dict()

        for nao_terminal in self.nao_terminais:
            self._firsts.update({nao_terminal: set()})

    def calcular_firsts(self) -> set:
        nullables = self.calcular_nullables()

        self._definir_firsts()

        # Caso trivial onde X -> aβ, em que a é terminal ou vazio
        # e β representa qualquer combinação contendo terminais ou nao terminais.
        for nao_terminal, producao in self.producoes.items():
            for derivacao in producao:
                primeiro_simbolo = derivacao[0]

                if primeiro_simbolo in self.terminais or primeiro_simbolo == STRING_VAZIA:
                    self._firsts[nao_terminal].add(primeiro_simbolo)

        # Caso onde X -> Aβ, onde A é não terminal e β representa qualquer combinação
        # contendo terminais ou nao terminais.
        for nao_terminal, producao in self.producoes.items():
            for derivacao in producao:
                primeiro_simbolo = derivacao[0]

                if primeiro_simbolo in self.nao_terminais:
                    print()
                    print('nao_terminal = ', nao_terminal)
                    print('derivacao = ', derivacao)
                    print(
                        f'primeiro_simbolo = {primeiro_simbolo} : nullable = {nullables[primeiro_simbolo]}')

                    if not nullables[primeiro_simbolo]:
                        self._firsts[nao_terminal] = self._firsts[nao_terminal].union(
                            self._firsts[primeiro_simbolo])
                    else:
                        pass

                    print(
                        f'First({primeiro_simbolo}) = {self._firsts[primeiro_simbolo]}')
                    print(
                        f'First({nao_terminal}) = {self._firsts[nao_terminal]}')
                    print()

        return self._firsts
