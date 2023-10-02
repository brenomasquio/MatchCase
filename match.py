num = int(input("Digite 1 ou 2: "))
match num :
    case 1:
        print("Digitou 1")
    case 2:
        print("Digitou 2")
    case _:
        print("Digito errado")


#composta

login = str(input("Digite seu login: "))
senha = str(input("Digite a sua senha: "))
match(login, senha):
    case ("Breno", "123"):
        print("Logado com sucesso")
    case _:
        print("Login ou senha incorreto")