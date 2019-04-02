salm=[]
salf=[]
m=0
f=0
for i in range(1,11):
    sal=int(input())
    sex=str(input())
    if(sex=='m'):
        m+=1
        salm.append(sal)
    if(sex=='f'):
        f+=1
        salf.append(sal)
x=(sum(salm)+sum(salf))
y=(len(salm)+len(salf))

print(m)
print(f)
print(x/y)
if(max(salm)>max(salf)):
    print('m')
if(max(salm)<max(salf)):
    print('f')
k=(sum(salm)/len(salm))
#kl=float(k)
print('%.1f'%k)
