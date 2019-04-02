maior = 0
nmm = 0
for i in range(5):
    n = int(input())
    soma = 0
    for j in range(1, n + 1):
        if (n % j == 0):
            soma += j
    if (soma > maior):
        maior = soma
        nm = n
print(nm)
