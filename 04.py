# Refatorar
# a. Feita a questão 3 crie uma função calcular que recebe 3 parâmetros:
# i. numero1, numero2 e operação (pode ser somar; subtrair; multiplicar e dividir)

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    
def calcular(numero1, numero2, operacao):
    if operacao == 1:
        somar(numero1, numero2)
        print(f'SOMA: {numero1} + {numero2} = {somar(numero1, numero2):.2f}')
    if operacao == 2:
        subtrair(numero1, numero2)
        print(f'SUBTRAÇÃO: {numero1} - {numero2} = {subtrair(numero1, numero2):.2f}')
    if operacao == 3:
        multiplicar(numero1, numero2)
        print(f'MULTIPLICAÇÃO: {numero1} * {numero2} = {multiplicar(numero1, numero2):.2f}')
    if operacao == 4:
        dividir(numero1, numero2)
        if numero2 == 0:
            print(f'DIVISÃO: {numero1} / {numero2} = Erro! Não existe divisão por zero')
        else:    
            print(f'DIVISÃO: {numero1} / {numero2} = {dividir(numero1, numero2):.2f}')
    
while(True):
    try:
        numero1 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Valor inválido! Digite um número")
    
while(True):
    try:
        numero2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Valor inválido! Digite um número")

while(True):
    try:
        operacao = int(input("Digite a operação desejada:\n1 - ADIÇÃO\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n"))
        if ((operacao != 1) or (operacao != 2) or (operacao != 3) or (operacao != 4)):
            print("Valor inválido! Digite 1, 2, 3 ou 4")

        if ((operacao == 1) or (operacao == 2) or (operacao == 3) or (operacao == 4)):
            calcular(numero1, numero2, operacao)
            break
    except ValueError:
        print("Valor inválido! Digite 1, 2, 3 ou 4")