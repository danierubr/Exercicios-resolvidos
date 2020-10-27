quant = int(input())
for v in range(quant):
    alunos = int(input())
    fila = list(map(int, input().split()))
    filaordenada = sorted(fila, reverse=True)
    cont = 0
    for ind in range(0, len(fila)):
        if fila[ind] == filaordenada[ind]:
            cont += 1
    print(cont)
