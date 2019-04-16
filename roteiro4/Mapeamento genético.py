seq = input()
base= input()
qtd =0
mai =0
b=0
if base not in seq:
    print('ERRO')
else:
    for p in range(len(seq)):
        if seq[p]==base:
            qtd+=1
        if qtd>mai:
            mai=qtd
            b = p-(qtd-1)
        if seq[p]!=base and qtd!=0:
            qtd=0
    print(b)
    print(mai)
