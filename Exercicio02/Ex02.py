casos = int(input())
for i in range(casos):
    n, P, Q = map(int, input().strip().split(sep=" "))
    ovos = list(map(int, input().strip().split(sep=" ")))

    ovos.sort()

    peso = 0
    quant_ovos = 0

    for ovo in ovos:
        if quant_ovos < P and peso + ovo <= Q:
            peso += ovo
            quant_ovos += 1
        else: 
            break
    print(f"Caso {i+1}: {quant_ovos}")
    