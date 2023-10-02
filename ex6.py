str1 = str(input("Digite a string 1: "))
str2 = str(input("Digite a string 2: "))

match str1, str2:
    case ("hello",_):
        print("A primeira string é 'hello' e a segunda é qualquer outra coisa.")
    case (_, "world"):
        print("A segunda string é 'world' e a primeira é qualquer outra coisa.")
    case (string2,string1):
        print("Ambas as strings são iguais.")
    case _:
        print("Nenhuma das condições é satisfeita.")