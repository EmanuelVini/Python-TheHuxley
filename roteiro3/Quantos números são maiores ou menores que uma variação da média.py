n=int(input())
i=1
lx=[]
cont=0
contx=0
for i in range(n):
    v=int(input())
    lx.append(int(v))
med=sum(lx)/len(lx)
for i in range(len(lx)):
    if lx[i]>med*1.1:
        cont+=1
    if lx[i]<med*0.9:
        contx+=1
#med=sum(lx)/len(lx)
print('%.2f'%med)
#print(lx)
print(cont)
print(contx)
