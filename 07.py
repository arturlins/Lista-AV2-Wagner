# Escreva uma função que calcule o fatorial de um número inteiro não-negativo.

def fatorial(numero):
    i = 1
    fatorado = 1
    while i <= numero:
          fatorado = fatorado * i
          i = i + 1
    return(fatorado)

while(True):
    try:
        numero = int(input('Digite um número inteiro positivo: '))
        if numero > 0:
            print(f'O fatorial de {numero} é {fatorial(numero)}')
            break
        if numero == 0:
            print(f'O fatorial de 0 é 1')
            break
        if numero < 0:
            print("Valor inválido! Digite um número inteiro positivo")
    except ValueError:
        print("Valor inválido! Digite um número inteiro positivo")