# Escreva uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def len_inteiro(numero):
    return len(str(numero))

while(True):
    try:
        numero = int(input("Digite um número inteiro: "))
        print(len_inteiro(numero))
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro!")