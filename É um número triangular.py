n = int(input())
var=0
if(n>0):
    for i in  range(1,n+1):
        var =((i-1)*(i)*(i+1))
        if(var==n):
            print('{} * {} * {} = {}'.format(i-1,i,i+1,n))
            print('Verdadeiro')
            break
    if(var!=n):
        print('Falso')
else:
    print('Falso')
