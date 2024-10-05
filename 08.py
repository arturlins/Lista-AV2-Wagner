# Escreva uma função que receba um número e retorne True se ele for primo e False caso contrário.

def numero_primo(numero):
    primo = True

    for i in range (2, numero):
        if numero % i == 0:
            primo = False
            break
    return primo

while(True):
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero < 0:
            print("Valor inválido! Não existe número primo negativo")
            break
        if numero == 1 or numero == 0:
            print(f'O número {numero} não é primo')
            break
        if numero_primo(numero) == False:
            print(f'O número {numero} não é primo')
            break
        if numero_primo(numero) == True:
            print(f'O número {numero} é primo')
            break
    except ValueError:
        print("Valor inválido!")