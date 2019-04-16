contc, contb = 0, 0
for i in range(6):
    e = input()
    if(e.upper()=="CINEMA"):contc +=1
    else: contb +=1
if(contc > contb):
    print("CINEMA")
else:
    print("BOLICHE")
