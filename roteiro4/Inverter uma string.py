Palavra = input()
novaPalavra = ''

for i in range(len(Palavra)-1, -1, -1):
    novaPalavra += Palavra[i]
print (novaPalavra)
