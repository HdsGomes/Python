#



print("Programa para calcular notas bimestrais")
b1 = float(input("digite a nota do 1º bimestre (Valor maximo 25)"))
b2 = float(input("digite a nota do 2º bimestre (Valor maximo 25)"))
b3 = float(input("digite a nota do 3º bimestre (Valor maximo 25)"))
b4 = float(input("digite a nota do 4º bimestre (Valor maximo 25)"))

resultado = b1+b2+b3+b4
print("O resultado total é",resultado)

if(resultado>59 and resultado <101):
    print("O aluno está aprovado!")
elif(resultado >=40 and resultado < 60):
    print("O aluno está de recuperação!")
elif(resultado < 40 and resultado >=0):
    print("O aluno está reprovado!")
else:
    print("Confirme os valores digitados, valor inválido!!!!")

