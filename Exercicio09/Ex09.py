def eh_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def busca(k, ultimo, resto):
    if k == 1:
        if resto > ultimo and eh_primo(resto):
            return [resto]
        return None
    p = ultimo + 1
    while p * k <= resto:
        if eh_primo(p):
            r = busca(k - 1, p, resto - p)
            if r is not None:
                return [p] + r
        p += 1
    return None

t = int(input())
for _ in range(t):
    n = int(input())
    k = 1
    while True:
        res = busca(k, 1, n)
        if res is not None:
            senha = ""
            for x in res:
                senha += str(x)
            print(senha)
            break
        k += 1