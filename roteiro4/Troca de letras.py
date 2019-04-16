pn=str(input())
lx=[]
pa=[]
lop=['SAIR','FIM','F1M','541r']
#3,4,5,1
while pn!=lop:
    pa=pn.upper()
    for i in range(len(pa)):
        if pa[i]=='3':
            lx.append('E')
        if pa[i]=='4':
            lx.append('A')
        if pa[i]=='5':
            lx.append('S')
        if pa[i]=='1':
            lx.append('I')
        elif pa[i]!='3' or '4' or '5' or '1':
            lx.append(pa[i])
    if '3' in lx:
        lx.remove('3')
    if '4'in lx:
        lx.remove('4')
    if '5'in lx:
        lx.remove('5')
    if '1' in lx:
        lx.remove('1')
    for i in range(len(lx)):
        print(lx[i],end=' ')
    pa=str(input())
