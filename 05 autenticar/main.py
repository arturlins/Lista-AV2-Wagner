from controlador_usuario import autenticar

print("Sistema de autenticação")
print("1 - Fazer login")
print("2 - Sair do sistema")

while True:
    try:
        opc = int(input("Escolha a opção: "))
        if opc == 1:
            login = input("Digite o nome do usuário: ")
            senha = input("Digite a senha: ")
            autenticar(login, senha)
            break
        if opc == 2:
            break
        if opc != 1 and opc != 2:
            print("Valor inválido")
    except ValueError:
        print("Valor inválido")