while(True):
    de =int(input())
    if(de<=0 or de >=10):
        print('Insira um n�mero inicial entre 1 e 9')
    else:
        break
while(True):
    ate=int(input())
    if(ate<=0 or ate>=10):
        print('Insira um n�mero final entre 1 e 9')
    else:
        break
if de <=ate:
    for i in range(de, ate+1):
        for j in range(1,10):
            print('%d x %d = %d' %(i,j,i*j))
        if i !=ate: print()   
elif de >ate:
    print('Nenhuma tabuada nesse intervalo')
