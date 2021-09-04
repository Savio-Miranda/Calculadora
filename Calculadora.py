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


programa_rodando = True
LISTA_DE_SIMBOLOS_ARITMETICOS = ['+', '-', '*', '/']
while programa_rodando:
    # Estado 1: Verificando se a variável 'numero_1' é um dígito.
    numero_1 = ''
    # While é uma espécie de limitador que, ao chegar ao fim sua identação
    # e o seu objetivo permanecer inconcluído, ele retorna para a sua
    # linha original para repetir o looping.
    while not numero_1.isdigit():
        numero_1 = input('Digite um número: ')
        if not numero_1.isdigit():
            print(numero_1, ' parece um número pra ti, cuzão ou cuzona?')
    # Estado 2: Verificando se a variável 'escolha' possui um símbolo válido.
    escolha = ''
    # O uso de uma função é bastante simples até. Como na matemática, toda função
    # em Python possui um parâmetro. Ele é uma 'caixa' que recebe um valor
    # toda vez que a função é chamada em uma linha de código. Isso
    # significa que a função tem um objetivo principal (e idealmente único).
    # Assim, quando se quer realizar uma mesma operação em diversos Estados de
    # um código, podemos simplesmente chamar uma função em cada um desses pontos
    # para deixá-lo mais limpo, organizado e eficiente.
    while not trata_de_um_simbolo_valido(escolha):
        # Note que a função 'trata_de_um_simbolo_valido' possui um parâmetro chamado
        # 'símbolo', de tal forma que ela executa a inclusão de 'simbolo' dentro
        # de uma lista chamada 'LISTA_DE_SIMBOLOS_ARITMÉTICOS'. Então ao substituir
        # 'simbolo' pela variável escolha, estamos dizendo que queremos a função
        # execute na nossa variável aquilo que está pré-programado na função.
        escolha = input('Digite qual operação entre eles deseja executar (+, -, *, /): ')
        if not trata_de_um_simbolo_valido(escolha):
            print('Coé, bota um dos símbolos aí, mano')
    # Estado 3: Verificando se a variável 'numero_2' é um dígito.
    numero_2 = ''
    while not numero_2.isdigit():
        numero_2 = input('Digite um número: ')
        if not numero_2.isdigit():
            print(numero_2, 'Não é um número, mano(a).')
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)
    # Estado 4: Verificar os símbolos e decidir qual operação realizar.
    if escolha == '+':
        print('{} + {} = {}'.format(numero_1, numero_2, soma(numero_1, numero_2)))
    if escolha == '-':
        print('{} - {} = {}'.format(numero_1, numero_2, subtracao(numero_1, numero_2)))
    if escolha == '*':
        print('{} * {} = {}'.format(numero_1, numero_2, multiplicacao(numero_1, numero_2)))
    if escolha == '/':
        print('{} / {} = {}'.format(numero_1, numero_2, divisao(numero_1, numero_2)))
    resposta = input('Deseja parar o programa?\nR = ')
    if resposta == 's':
        programa_rodando = False
print('Programa finalizado')
