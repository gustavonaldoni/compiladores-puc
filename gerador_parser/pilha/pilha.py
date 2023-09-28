class Pilha:
    def __init__(self) -> None:
        self.conteudo = []

    def esta_vazia(self) -> bool:
        return len(self.conteudo) == 0

    def topo(self) -> any:
        if self.esta_vazia():
            raise IndexError("Nao eh possivel ver o topo de uma pilha vazia ...")

        return self.conteudo[-1]

    def pop(self) -> any:
        if self.esta_vazia():
            raise IndexError("Nao eh possivel remover de uma pilha vazia ...")

        elemento = self.topo()
        self.conteudo = self.conteudo[:-1]

        return elemento

    def push(self, elemento: any):
        self.conteudo.append(elemento)
