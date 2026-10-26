import sys


def main():
    entrada = sys.stdin.read().split()
    pos = 0
    t = int(entrada[pos])
    pos += 1
    for _ in range(t):
        n = int(entrada[pos])
        pos += 1
        pesos = [int(x) for x in entrada[pos:pos + n]]
        pos += n
        lis = [1] * n
        lds = [1] * n
        melhor = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if pesos[j] > pesos[i] and lis[j] + 1 > lis[i]:
                    lis[i] = lis[j] + 1
                elif pesos[j] < pesos[i] and lds[j] + 1 > lds[i]:
                    lds[i] = lds[j] + 1
            melhor = max(melhor, lis[i] + lds[i] - 1)
        print(melhor)


main()