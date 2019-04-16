pa=str(input())
pa.upper()
cont=0
lx=[]
for i in range(len(pa)):
    lx.append(pa[i].upper())
    for j in range(len(lx)):
        print(lx[j],end='')
    print('')
