# Crie um programa que receba um numero digitado pelo usuário
# que será comparado se o numero digitado é maior que 10, igual a 10 ou menor
# que 10.

print("Programa advinha número")
num1 = int(input("digite o numero inteiro"))

if num1 > 10:
    print( "O número digitado é maior que o número secreto")
elif num1 < 10:
    print("O número digitado é menor que o número secreto")
else:
    print("Você acertou o número secreto")