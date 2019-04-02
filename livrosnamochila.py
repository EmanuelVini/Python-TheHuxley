liv = int(input())
cont=0
peso=0
while(liv<=18):
    cont+=1
    peso=peso+liv
    if(peso>=18):
        print(cont-1)
        break
    else:
        liv=int(input())
