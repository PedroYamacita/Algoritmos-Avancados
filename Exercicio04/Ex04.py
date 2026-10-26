import sys

def maior_soma_retanguar():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    
    n = int(entrada[0])
    
    matriz = []
    idx = 1
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(int(entrada[idx]))
            idx += 1
        matriz.append(linha)
        
    soma_maxima = float('-inf')
    
    for topo in range(n):
        temp = [0] * n
        
        for base in range(topo, n):
            for col in range(n):
                temp[col] += matriz[base][col]
            
            max_atual = temp[0]
            max_global = temp[0]
            
            for i in range(1, n):
                max_atual = max(temp[i], max_atual + temp[i])
                if max_atual > max_global:
                    max_global = max_atual
            
            if max_global > soma_maxima:
                soma_maxima = max_global
                
    print(soma_maxima)

if __name__ == '__main__':
    maior_soma_retanguar()