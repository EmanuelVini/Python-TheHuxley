nome = input()
nome = nome.split()
inv = False
for i in range(len(nome)):
    if(inv):
        nome[i] = (nome[i])[::-1]
        inv = False
    else:
            inv = True
print(" ".join(nome))
