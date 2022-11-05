#Faça um Programa que leia dois vetores com 10 posições cada e receba números inteiros.
# Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
# Mostre ao final os três vetores.

vet1 = []
vet2 = []
vet3 = []

print('Informe os valores do primeiro vetor')

for i in range(10):
    vet1.append(int(input('Informe um numero: ')))

print('Informe os valores do segundo vetor')

for i in range(10):
    vet2.append(int(input('Informe um numero: ')))

for i in range(10):
    vet3.append(vet1[i])
    vet3.append(vet2[i])
print(vet3)