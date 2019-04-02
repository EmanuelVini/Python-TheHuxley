n1 = int(input())
n2 = int(input())
if (n1 > n2):
    menor = n2
    n2 = n1
    n1 = menor
for i in range(n2, n1 - 1, -1):
    divs = 0
    primo = True
    for n in range(1, i):
        if (i % n == 0):
            divs += 1
        if (divs > 1):
            primo = False
    if (primo):
        if (i != 1):
            print(i)
