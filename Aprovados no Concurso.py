cont = 0
while True:
    qp = int(input())
    if (qp < 0):
        break
    qm = int(input())
    nr = float(input())
    if (qp >= 40) and (qm >= 21) and (nr >= 7):
        cont += 1
print(cont)
