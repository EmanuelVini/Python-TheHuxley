n=int(input())
ponto=n
ast=1
for i in range(1,n+1):
    print(ponto*'.'+ast*'*')
    ponto-=1
    ast=ast+2
ponto=1
ast=n*2-1
for i in range(1,n+1):
    print(ponto*'.' + ast*'*')
    ponto+=1
    ast=ast-2
