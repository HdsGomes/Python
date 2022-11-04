# Faça um programa para imprimir igual abaixo:
#1
#2 2
#3 3 3 ...
#n n n n ...
#“n” para um ”numero” (range) informado pelo usuário.
#• Use uma função que receba um valor n inteiro e imprima até a
#“n-Linha” informada pelo usuário.


def enes(n):
    for i in range(1, n + 1):
        cont = 1
        while True:
            print(i, end=' ')
            if cont == i:
                break
            cont += 1
        print()

n = int(input('Digite um número: '))
enes(n)