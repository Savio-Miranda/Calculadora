# I - Definindo o nome do modelo de calculadora
class CalculadoraModern2000:
    # II - Definindo o "construtor"
    def __init__(self):
        # III - O parâmetro "self" define uma variável global dentro de uma classe
        self.conj_operacoes = ['+', '-', '*', '/']
    # Função de checagem de operações
    def checar_operacao(self, op):
        operacao_valida = op in self.conj_operacoes
        return operacao_valida
    # Função de checagem de números
    def input_e_um_digito(self, num):
        if type(num) == str:
            return num.isdigit()
        if not type(num) == int and not type(num) == float:
            return False
        return True
    # Função central de cálculo contendo as operações
    def calcular(self, numero1, operacao, numero2):
        # Mas antes é preciso chamar as funções de filtragem de dados de input
        if not self.input_e_um_digito(numero1):
            return 'O primeiro número da operação não é válido: {}'.format(numero1)
        if not self.input_e_um_digito(numero2):
            return 'O segundo número da operação não é válido: {}'.format(numero2)
        if not self.checar_operacao(operacao):
            return 'A operação não é válida: {}'.format(operacao)
        # Fim da validação dos dados de input
        if operacao == '+':
            return numero1 + numero2
        elif operacao == '-':
            return numero1 - numero2
        elif operacao == '*':
            return numero1 * numero2
        elif operacao == '/':
            if numero2 == 0:
                return 'Não se pode dividir por 0...'
            return numero1 / numero2


