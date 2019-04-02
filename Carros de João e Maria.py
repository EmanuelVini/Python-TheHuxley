opt=str(input())
import sys
if(opt=='n'or opt=='N'):
    print('zero')
    #sys.exit
if(opt=='s'or opt=='S'):
    lano = []
    lvel = []
    while(opt=='s'or opt=='S'):
        ano = int(input())
        vel = float(input())
        opt=input()
        lano.append(ano)
        lvel.append(vel)
        if(opt=='N'or opt=='n'):
            print('%.2f'% max(lvel))
            print(max(lano))
            vmed=(sum(lvel))/(len(lvel))
            print('%.2f'%vmed)
            break
