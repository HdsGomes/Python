#



print("Programa para calcular notas bimestrais")
p1 = float(input("digite a nota da prova do 1º bimestre "))
p2 = float(input("digite a nota da prova do 2º bimestre "))
p3 = float(input("digite a nota da prova do 3º bimestre "))
p4 = float(input("digite a nota da prova do 4º bimestre "))

t1 = float(input("digite a nota do trabalho 1º bimestre "))
t2 = float(input("digite a nota do trabalho 2º bimestre "))
t3 = float(input("digite a nota do trabalho 3º bimestre "))
t4 = float(input("digite a nota do trabalho 4º bimestre "))

b1 = (p1+t1)/2
b2 = (p2+t2)/2
b3 = (p3+t3)/2
b4 = (p4+t4)/2

resultado = b1+b2+b3+b4

print("O média total é",resultado)

if(resultado>59 and resultado <101):
    print("O aluno está aprovado!")
elif(resultado >=40 and resultado < 60):
    print("O aluno está de recuperação!")
elif(resultado < 40 and resultado >=0):
    print("O aluno está reprovado!")
else:
    print("Confirme os valores digitados, valor inválido!!!!")

