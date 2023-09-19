class Producao:
    def __init__(self, lado_esquerdo: str, lado_direito: list[str]) -> None:
        self.lado_esquerdo = lado_esquerdo
        self.lado_direito = lado_direito

    def formatar_saida(self) -> str:
        resultado = f'{self.lado_esquerdo} -> '

        for derivacao in self.lado_direito:
            resultado += f'{derivacao} | '
        
        resultado = resultado[:-3]

        return resultado

    def mostrar(self):
        print(self.formatar_saida())