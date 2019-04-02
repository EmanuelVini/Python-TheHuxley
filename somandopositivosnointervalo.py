n1 = int(input())
n2 = int(input()) 
if(n1<n2):
    x=1
if(n1>n2):
    x=-1
soma = 0
if(n1<n2):
    for i in range (n1,n2+1,x):
        if(i>=0):
            soma+=1
    print(soma)
if(n1>n2):
    for i in range (n2,n1+1,x):
        if(i>=0):
            soma+=1
    print(soma)
