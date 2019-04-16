lista=[]
soma=0
tamanho = int(input())
if tamanho==0:
    print('Lista vazia - O valor de S eh zero')
elif tamanho<0:
    print('O valor informado para N foi negativo')
else:
    for valor in range(tamanho):
        lista.append(int(input()))
    listaInversa=lista[::-1]
    index=tamanho//2
    for i in range(index):
        soma+=(lista[i]-listaInversa[i])**2
    if tamanho%2!=0: soma+=lista[index]**2
    print('S =',soma)
