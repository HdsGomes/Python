

vetor = []

for i in range(10):
    consoante = input("digite uma letra de A - Z : ").upper()
    if consoante not in ["A","E","I","O","U"]:
        vetor.append(consoante)

print("O vetor possui ", len(vetor), "posições de consoantes lidas")
print("Consoantes digitadas: ", vetor)
