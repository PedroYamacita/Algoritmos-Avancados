import sys

def resolver():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    
    num_casos = int(entrada[0])
    idx = 1
    
    for _ in range(num_casos):
        n = int(entrada[idx])
        m = int(entrada[idx+1])
        idx += 2
        
        precos = []
        satisfacoes = []
        for _ in range(n):
            precos.append(int(entrada[idx]))
            satisfacoes.append(int(entrada[idx+1]))
            idx += 2
            
        limite_gasto = m + 200
        
        # dp[i] armazena a satisfação máxima obtida gastando-se exatamente 'i' reais
        dp = [-1] * (limite_gasto + 1)
        dp[0] = 0
        
        for i in range(n):
            p = precos[i]
            s = satisfacoes[i]
            for w in range(limite_gasto, p - 1, -1):
                if dp[w - p] != -1:
                    dp[w] = max(dp[w], dp[w - p] + s)
                        
        max_satisfacao = 0
        for w in range(limite_gasto + 1):
            if w <= m or (w > 2000 and w <= m + 200):
                if dp[w] > max_satisfacao:
                    max_satisfacao = dp[w]
                    
        print(max_satisfacao)

if __name__ == '__main__':
    resolver()