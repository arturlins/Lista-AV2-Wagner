# Crie uma função que receba uma string e retorne o número de vogais presentes na string

def vogais(texto):
    contador = 0
    for vogal in texto:
        if vogal in 'aeiouAEIOU': 
            contador += 1
    return contador

texto = input("Digite uma palavra ou frase: ")
print(f'A palavra/frase digitada tem {vogais(texto)} vogais')