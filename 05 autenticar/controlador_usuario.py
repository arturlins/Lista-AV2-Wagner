from os import system

usuarios = [
{
"username": "teste",
"password": "admin"
},
{
"username": "teste2",
"password": "admin2"
},
{
"username": "teste3",
"password": "admin3"
},
{
"username": "teste4",
"password": "admin4"
},
]

def autenticar(login, senha):
    validador = False
    for usuario in usuarios:
        if (usuario['username'] == login) and (usuario['password'] == senha):
            validador = True
            system('cls')
            print("Bem vindo ao sistema!")
    if validador == False:
        print("Login ou senha inválidos")