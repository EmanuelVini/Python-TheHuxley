c = input()
lx=[]
l7=[]
if len(c)==10:
    for i in range(len(c)):
        lx.append(c[i])
    l7.append(lx[6])
    if 'b' in l7:
        print('Bulbassauro')
    if 'c' in l7:
        print('Charmander')
    if 's' in l7:
        print('Squirtle')
    elif l7[0]!='b' and l7[0]!='c' and l7[0]!='s':
        print('Codigo Invalido')
        #if lx[i] == 'b':
           # print('Bulbassauro')
       # if lx[i] == 'c':
           # print('Charmander')
        #if lx[7] == 's':
            #print('Squirtle')
else:
    print('Codigo Invalido')
