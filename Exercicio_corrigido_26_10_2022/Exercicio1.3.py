# Crie um programa para receber dois números e realizar
# todas operações matemáricas, e ao final mostrar todos os results
# incluindo resto da divisao e exponencial
print("Programa para calcular operações matemáticas")
num1=float(input("digite o primeiro numero inteiro da operação: "))
num2=float(input("digite o segundo numero inteiro da operação: "))
resultado  = num1 + num2
resultado2 = num1 - num2
resultado3 = num1 * num2
resultado4 = num1 / num2
resultado5 = num1 % num2
resultado6 = num1 ** num2

print("A soma de", num1, "+",num2,"é igual a: ",resultado)
print("A subtração de", num1, "por",num2,"é igual a: ",resultado2)
print("A multipicação de", num1, "por",num2,"é igual a: ",resultado3)
print("A divisão de", num1, "por",num2,"é igual a: ",resultado4)
print("O resto da divisão de ", num1, "por", num2, "é igual a ",resultado5)
print("A potencia de", num1, "elevado a ",num2,"é igual a: ",resultado6)