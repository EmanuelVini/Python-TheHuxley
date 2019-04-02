while(True):
    quantidade= int(input())
    if(quantidade ==0): break
    cont, a, b, saida = 1, 0, 1, '0'
    while cont < quantidade:
        cont,a, b = cont+1, b, a+b
        saida+= ' ' +str(a)
    print(saida)
