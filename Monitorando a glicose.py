n = float(input())
cont = 0
qt = 0
while(n>0):
    cont+=n
    qt+=1
    n = float(input())
med=(cont/qt)
if(med>=200):
    print('Glicose Muito Alta')
if(med<=110):
    print('Glicose Normal')
if(med>110)and(med<200):   
    print('Glicose Alterada')
