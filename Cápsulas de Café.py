sum = 0
for i in range(7):
    n = int(input())
    t = input()
    t = t.upper()
    if (t == "P"):
        sum += n * 10
    else:
        sum += n * 16
qx = sum // (3.5)
print(sum)
print(round(qx))
