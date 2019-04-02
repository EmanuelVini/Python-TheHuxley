num = int(input())
nump = []
for i in range(6, num):
    soma = 0
    for l in range(1, i):
        if (i % l == 0):
            soma += l
    if (soma == i):
        print(i)
