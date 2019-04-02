n=int(input())
if(n>=1)and(n<=1000):
    for c in range (1,n+1):
        print('{} {} {}'.format(c , c*c, c**3))
