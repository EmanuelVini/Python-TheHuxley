n=int(input())
lx=[]
if n>5 or n<=0:
    print('Numero de notas invalido.')
else:
    if n<=5 or n>0:
        for i in range(n):
            notas=float(input())
            lx.append(float(notas))
        for c in range(len(lx)):
            #print('Nota',c+1,':',lx[c])
            print('Nota {}: {}'.format(c+1,lx[c]))
            med=(sum(lx)/len(lx))
        print('Media: %.2f'%med)

#else:
    #print('N�mero de notas invalido.')
