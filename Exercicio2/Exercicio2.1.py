# Crie um programa receba 5 produtos em variáveis constantes, iPhone, Samsung, Tablet, PS5, notebook , com valores respectivos de R$ 2980, R$ 2540, R$ 1950, R$ 2100, R$ 2350.
# O usuário deverá informar a quantidade de cada produto que ele deseja comprar em sua loja, caso não queira nenhum produto deverá informar o valor 0 (zero) de quantidade.
# Ao final da compra mostre o valor total de todos os produtos.
# O valor da parcela dividido em 3X sem juros.
# O valor da parcela dividido em 6X com acréscimo de 5%.
# E um valor com 10% de desconto para pagamento à vista.

iphone = float(2980)
Samsung = float(2540)
Tablet = float(1950)
PS5 = float(2100)
Notebook = float(2350)

Qiphone = float(input("digite o número de iphones que deseja comprar: "))
Qsamsung = float(input("digite o número de samsumgs que deseja comprar: "))
Qtablet = float(input("digite o número de Tablets que deseja comprar: "))
Qps5 = float(input("digite o número de Playstation 5 que deseja comprar: "))
Qnotebook = float(input("digite o número de Notebooks que deseja comprar: "))

totaliphone = iphone*Qiphone
totalsamsung = Samsung*Qsamsung
totaltablet = Tablet*Qtablet
totalps5 = PS5*Qps5
totalsnotebook = Notebook*Qnotebook

print("O valor total de Iphones é: ",totaliphone)
print("O valor total de Samsumgs é: ",totalsamsung)
print("O valor total de Tablets é: ",totaltablet)
print("O valor total de Playstations 5 é: ",totalps5)
print("O valor total de notebooks é: ",totalsnotebook)

totalprodutos = totaliphone+totalsamsung+totaltablet+totalps5+totalsnotebook
totalprodutos5 = totalprodutos*1.05
totalavista = (totalprodutos)-(totalprodutos*0.1)

print("o valor total dos produtos é:",totalprodutos)
print("o valor de cada parcela se dividido em 3x sem juros é: ", totalprodutos/3)
print("o valor de cada parcela se dividido em 6x com acréscimo de 5%: ", totalprodutos5/6)
print("o valor do produto se pago à vista com desconto de 10%", totalavista)



