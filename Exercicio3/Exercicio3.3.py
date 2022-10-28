#Crie um programa de calculadora que realiza as operações de
#soma, multiplicação, divisão e subtração, será perguntado ao
#usuário se deseja continuar com o uso da calculadora, enquanto
# ele digitar (“S” – Sim) o programa irá reiniciar a calculadora.

opcao = "S"
while opcao == "S":
    numero1 = float(input("escolha o primeiro numero para operacao:"))
    numero2 = float(input("escolha o segundo numero para a operacao:"))
    print("O resultado da soma é", float(numero1) + float(numero2))
    print("O resultado da subtração é", float(numero1) - float(numero2))
    print("O resultado da multiplicação é", float(numero1) * float(numero2))
    print("O resultado da divisao é", float(numero1) / float(numero2))

    opcao= input("você deseja continuar? Caso sim, digite S")
    print("Fim do Código")