#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
# que já é um sucesso na sua loja de 1,99.
# Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães,
# a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

#Preço do pão será informado pelo usuário: se informar que custa R$ 0.18
#Mostrará a tabela abaixo:


print("PROGRAMA TABELA DE PAES")
precoPao=float(input("Qual o Preço dos Pães? "))

print("Tabela de Preços 50 paes a", precoPao)
for i in range(1,51):
    print(i , "Pães = R$",(precoPao*(i)))
