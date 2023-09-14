def formatar_tokens() -> list:
    tokens_antes = ("auto", "double", "int", "struct", "break",
                    "else", "long", "switch", "case", "enum", "register",
                    "typedef", "char", "extern", "return", "union", "const",
                    "float", "short", "unsigned", "continue", "for", "signed",
                    "void", "default", "sizeof", "volatile", "do", "if", "static",
                    "while", 'ge', 'le', 'eq', 'ne',
                    'num', 'id')

    tokens_depois = []

    for token in tokens_antes:
        token = token.upper()
        tokens_depois.append(token)

    return tokens_depois

def gerar_arquivo_tokens(tokens: list):
    i = 257

    with open('tokens.h', mode='w+') as file:
        for token in tokens:
            texto = f'#define {token} {i}\n'
            file.write(texto)

            i += 1

def formatar_tokens_analex(tokens: list):
    resultado = ''

    for token in tokens:
        resultado += f'"{token.lower()}" {{ return {token}; }} \n'

    return resultado

if __name__ == '__main__':
    tokens = formatar_tokens()
    tokens_analex = formatar_tokens_analex(tokens)

    print(tokens_analex)
    gerar_arquivo_tokens(tokens)
    