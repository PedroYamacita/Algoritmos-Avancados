def verifica_disponibilidade(meio, duracoes, K):
    dias = 1
    soma_atual = 0

    for d in duracoes:
        if soma_atual + d > meio:
            dias += 1
            soma_atual = d
        else:
            soma_atual += d

    return dias <= K

N = int(input().strip())
for caso in range(1, N+1):
    T, K = map(int, input().strip().split())
    duracoes = list(map(int, input().strip().split(sep=" ")))

    minimo = max(duracoes)
    maximo = sum(duracoes)
    resposta = maximo

    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if(verifica_disponibilidade(meio, duracoes, K)):
            resposta = meio
            maximo = meio - 1
        else:
            minimo = meio + 1

    print(f"Caso {caso}: {resposta}")