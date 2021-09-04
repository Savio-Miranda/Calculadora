def soma(valor_1, valor_2):
    return valor_1 + valor_2


def subtracao(valor_1, valor_2):
    return valor_1 - valor_2


def multiplicacao(valor_1, valor_2):
    return valor_1 * valor_2


def divisao(valor_1, valor_2):
    if valor_2 == 0:
        return 'Tá de sacanagem, mermão? Quer dividir por 0 mesmo? Olha a audácia desse fdp'
    else:
        return valor_1 / valor_2


def trata_de_um_simbolo_valido(simbolo):
    return simbolo in LISTA_DE_SIMBOLOS_ARITMETICOS


