#Crie um programa para realizar as operações de uma tabuada de multiplicação, onde será solicitado ao usuário digitar qual
#numero será a tabuada e qual intervalo do inicio e fim da
#tabuada, e exibir na tela o resultado conforme intervalo.

print("PROGRAMA TABUADA MULTIPLICAÇÃO")
numero=int(input("Qual Número voce quer saber a tabuada? "))
inicio = int(input("digite o inicio do intervalo da tabuada:" ))
fim = int(input("digite o fim do intervalo da tabuada:" ))

print("Tabuada de", numero, "de", inicio, "até",fim)
for i in range(inicio,fim):
    print(numero, '*', i , "=",(numero*(i)))
