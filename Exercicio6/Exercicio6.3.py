#Numa fazenda em um local reservado para criação coloca-se um casal de coelhos.
# Supondo que em cada mês, a partir do segundo mês de vida, cada casal dá origem a um novo casal
# de coelhos, ao fim de um ano, quantos casais de coelhos estão no pátio?
# Escreva um programa para calcular a quantidade de coelhos em um ano

nmeses = int(input("Qual a quantidade de meses que se passaram? "))


def fibonacci(nmeses):
   if nmeses >0 and nmeses <3:
       return 1
   else:
       return fibonacci(nmeses -1) + fibonacci(nmeses - 2)


for i in range(nmeses):
   casal = fibonacci(i+1)
   print("O numero de casal de coelhos no mês",i+1,"é: ", casal)
