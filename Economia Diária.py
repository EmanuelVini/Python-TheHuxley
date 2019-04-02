cont = 0
sum = 0
meta = 0
for i in range(7):
    val = float(input())
    if (i == 0):
        meta = val
    elif (val >= meta):
        cont += 1
    sum += val
    meta = val + 0.5
print("R$ " + "%.2f" % sum)
print(cont)
