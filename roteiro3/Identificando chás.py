t=int(input())
res=input().split()
lx=[]
cont=0
for i in range(len(res)):
    lx.append(int(res[i]))
for i in range(len(lx)):
    if(lx[i]==t):
        cont+=1
print(cont)
