n = int(input())
for i in range(n):
    nome = input().upper().replace(" ","")
    if(nome == nome[::-1]):
        print("SIM")
    else:
        print("NAO")
