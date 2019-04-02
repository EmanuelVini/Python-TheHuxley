n=int(input())
cont=0
while(n>=0):
    for i in range(1,n+1):
        if(n%i==0):
            cont+=1
    if(cont==2):
        print('1')
    else:
        print('0')
    cont=0
    n=int(input())
    #if(n==0):
        #print('0')
    if(n<0):
        break
