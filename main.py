from Modern import CalculadoraModern2000
programa_rodando = True
calc = CalculadoraModern2000()
while programa_rodando:
    numero1 = input('Digite um número inicial: ')
    operacao = input('Digite uma operação matemática do tipo "+", "-", "*", "/": ')
    numero2 = input('Digite um número final: ')
    resultado = calc.calcular(numero1, operacao, numero2)
    print('O resultado é:', resultado)
    stop = input('Digite "S" para parar. Senão, qualquer digito prosseguirá: ')
    if stop.upper() == 'S':
        break
print('Programa finalizado')
