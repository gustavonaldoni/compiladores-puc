import re

def validar_simbolo_inicial(simbolo_inicial: str) -> bool:
    return simbolo_inicial.isalpha()

def validar_nao_terminais(nao_terminais: str) -> bool:
    nao_terminais = nao_terminais.strip()
    nao_terminais = re.sub(r'\s+', '', nao_terminais)
    nao_terminais = nao_terminais.split(',')
    
    for nao_terminal in nao_terminais:
        if len(nao_terminal) > 1 or len(nao_terminal) == 0:
            return False
        
    return True

def validar_terminais(terminais: str) -> bool:
    return validar_nao_terminais(terminais)

def validar_regras_producao(regras_producao: str) -> bool:
    return True