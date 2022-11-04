#Faça um programa para ler o nome de 2 times e o número de gols marcados na partida (para cada time).
# Escrever o nome do vencedor e o resultado da partida.
# Caso não haja vencedor deverá ser impressa a palavra EMPATE.
# Ao final perguntar se deseja repetir a operação com novos times.

print("ALGORITMO PLACAR")


time1 = input("Escreva o nome do primeiro time: ")
golst1 = int(input("insira a quantidade de  gols marcados pelo time " + time1 + ": "))
time2 = input("Escreva o nome do segundo time: ")
golst2 = int(input("insira a quantidade de  gols marcados pelo time " + time2 + ": "))
fas
print("Placar Final: ", time1 , golst1 , "x" , golst2, time2)

if (golst1 > golst2):
    print("O vencedor da partida é o " + time1)
elif (golst1 < golst2):
    print("O vencedor da partida é o " + time2)
else:
   print("A partida terminou em EMPATE")