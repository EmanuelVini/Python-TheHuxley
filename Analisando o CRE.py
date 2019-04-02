menor = None
mmenor = " "
soma = 0
cont = 0
while True:
    mat = str(input())
    if (mat == "999"):
        break
    cre = float(input())
    soma += cre
    cont += 1
    if not menor or (cre < menor):
        menor = cre
        mmenor = mat

print(mmenor)
media = soma / cont
print("%.2f" % media)
