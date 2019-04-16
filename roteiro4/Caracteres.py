tam= int(input())
while tam> 0:
    palavra = input()
    novaPalavra = ''
    for i in range(tam-1, -1, -1):
        novaPalavra += palavra[i]
    print (novaPalavra)
    tam = int(input())
