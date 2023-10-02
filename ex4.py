animal = input("Digite um animal: ")

match animal:
    case "vaca":
        print("O animal é uma vaca")
    case "galinha":
        print("O animal é uma galinha")
    case "ovelha":
        print("O animal é uma ovelha")
    case _:
        print("Animal desconhecido")