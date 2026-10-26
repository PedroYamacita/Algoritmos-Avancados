import sys


def maior_fator_primo(n):
    maior = 1
    while n % 2 == 0:
        maior = 2
        n //= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            maior = d
            n //= d
        d += 2
    if n > 1:
        maior = n
    return maior


def main():
    entrada = sys.stdin.read().split()
    t = int(entrada[0])
    for i in range(1, t + 1):
        print(maior_fator_primo(int(entrada[i])))


main()