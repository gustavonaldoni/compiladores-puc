from gramatica.gramatica import Gramatica, SIMBOLO_EOF, SIMBOLO_VAZIO
from tabela_parse.tabela_parse import TabelaParse
from pilha.pilha import Pilha


class AnalisadorSintaticoPreditivo:
    def __init__(self, gramatica: Gramatica) -> None:
        self.gramatica = gramatica

        self.tabela_parse = TabelaParse(gramatica)
        self.tabela_parse.construir()

        self.pilha = Pilha()
        self.input = ""
        self.output = ""

    def _inicializar_pilha(self):
        self.pilha.push(SIMBOLO_EOF)
        self.pilha.push(self.gramatica.simbolo_inicial)

    def _inicializar_input(self, input: str):
        self.input = f"{input}{SIMBOLO_EOF}"

    def _inicializar_output(self):
        self.output = ""

    def _inicializar(self, input: str):
        self._inicializar_pilha()
        self._inicializar_input(input)
        self._inicializar_output()

    def _mostrar_estado_atual(self):
        print()
        print(f"Pilha: {self.pilha.conteudo}")
        print(f"Input: {self.input}")
        print(f"Output: {self.output}")

    def analisar(self, input: str) -> bool:
        self._inicializar(input)

        while True:
            self._mostrar_estado_atual()

            nao_terminal = self.pilha.pop()
            terminal = self.input[0]

            producao = self.tabela_parse.tabela[(nao_terminal, terminal)]
            self.output = producao

            if len(producao) == 0:
                return False

            producao_ao_contrario = [elemento[::-1] for elemento in producao]

            for derivacao in producao_ao_contrario:
                for simbolo in derivacao:
                    if simbolo != SIMBOLO_VAZIO:
                        self.pilha.push(simbolo)

            if self.pilha.topo() == self.input[0] and self.pilha.topo() != SIMBOLO_EOF:
                self._mostrar_estado_atual()

                self.pilha.pop()
                self.input = self.input[1:]

            if len(self.pilha.conteudo) == 1:
                self._mostrar_estado_atual()
                break

            if self.input == SIMBOLO_EOF:
                continue

        if self.pilha.conteudo[0] == self.input and self.input == SIMBOLO_EOF:
            return True
