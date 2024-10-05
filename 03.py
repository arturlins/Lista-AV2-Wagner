# Crie uma calculadora utilizando funções
# a. Obrigatoriamente você deve ter funções: somar; subtrair; multiplicar e dividir
# i. Todas recebem 2 números como parâmetro de entrada

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    
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

print(f'SOMA: {numero1} + {numero2} = {somar(numero1, numero2):.2f}')
print(f'SUBTRAÇÃO: {numero1} - {numero2} = {subtrair(numero1, numero2):.2f}')
print(f'MULTIPLICAÇÃO: {numero1} * {numero2} = {multiplicar(numero1, numero2):.2f}')
if numero2 == 0:
    print(f'DIVISÃO: {numero1} / {numero2} = Erro! Não existe divisão por zero')
else:    
    print(f'DIVISÃO: {numero1} / {numero2} = {dividir(numero1, numero2):.2f}')