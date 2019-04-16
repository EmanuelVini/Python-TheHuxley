n = int(input())
for j in range(n):
    pal = input()
    while 1:
        controle = True
        for i in range(len(pal)):
            if(i+1 < len(pal)):
                if(pal[i] == pal[i+1]):
                    pal = pal[:i] + pal[(i+1):]
                    controle = False
        if(controle): break
    print(pal)
