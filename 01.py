# Faça um programa, com uma função que necessite de um parâmetro “número”. 
# A função retorna o valor de caractere ‘P’, se seu valor for positivo,
# e ‘N’, se seu valor for zero ou negativo

def positivo(numero):
    if numero >= 0:
        valor = 'P'
    if numero < 0:
        valor = 'N'
    
    return valor

while(True):
    try:
        numero = int(input("Digite um número inteiro: "))
        print(positivo(numero))
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro!")



