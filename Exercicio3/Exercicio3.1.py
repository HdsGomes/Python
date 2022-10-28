#Crie um programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Algoritmo  Turno")
print("Digite abaixo o turno que você estuda: M-matutino ou V-Vespertino ou N-Noturno")

turno = input()

match turno:
    case "M":
        print("Bom dia!")
    case "V":
        print("Boa tarde!")
    case "N":
        print("Boa Noite!")
    case _:
        print("Valor Inválido")
