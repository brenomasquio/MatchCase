cor = str(input("Digite uma cor: "))
match cor :
    case 'vermelho':
        print("Cor Vermelha")
    case 'azul':
        print("Cor Azul")
    case 'verde':
        print("Cor Verde")
    case _:
        print("Cor desconhecida")