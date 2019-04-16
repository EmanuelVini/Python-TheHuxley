tban = int(input())
cont= 0
ban= [0 , 0]
for i in range (tban):
    iban = input()
    iban = iban.split()
    ban[0] = int(iban[0])
    ban[1] = int(iban[1])
    if ban[0] > ban[1]:
        cont+= ban[1]
print (cont)
