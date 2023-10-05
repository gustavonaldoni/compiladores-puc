def formatar_tokens() -> list:
    tokens_antes = ("auto", "double", "int", "struct", "break",
                    "else", "long", "switch", "case", "enum", "register",
                    "typedef", "char", "extern", "return", "union", "const",
                    "float", "short", "unsigned", "continue", "for", "signed",
                    "void", "default", "sizeof", "volatile", "do", "if", "static",
                    "while", 'ge', 'le', 'eq', 'ne', 'not')

    tokens_depois = []

    for token in tokens_antes:
        token = token.upper()
        tokens_depois.append(token)

    return tokens_depois

def formatar_tokens_sint(tokens: list):
    resultado = ''
    tokens_excecoes = {'GE': '>=',
                       'LE': '<=',
                       'EQ': '==',
                       'NE': '!=',
                       'NOT': '!'}

    for token in tokens:
        if token in tokens_excecoes.keys():
            valor = tokens_excecoes.get(token)

        resultado += f'%token {token}\n'

    return resultado

if __name__ == '__main__':
    tokens = formatar_tokens()
    tokens_sint = formatar_tokens_sint(tokens)

    print(tokens_sint)
    