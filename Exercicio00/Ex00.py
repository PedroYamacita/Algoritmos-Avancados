def resolver_comando(comando, comandos):
    if comando == "ESQUERDA":
        return -1
    if comando == "DIREITA":
        return 1
    if comando.startswith("REPETE "):
        a, indice = comando.split()
        indice = int(indice)
        return resolver_comando(comandos[indice], comandos)
    return 0


pedidos = int(input().strip())

for i in range(pedidos):
    ncomandos = int(input().strip())
    comandos = [input().strip() for i in range(ncomandos)]
    x = 0

    for comando in comandos:
        x += resolver_comando(comando, comandos)

    print(x)
