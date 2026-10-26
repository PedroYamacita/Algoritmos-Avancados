import sys

def prisioneiros():
    entrada = sys.stdin.read().split()
    
    if not entrada:
        return
        
    numero_casos = int(entrada[0])
    idx = 1
    
    for _ in range(numero_casos):
        comprimento_prancha = int(entrada[idx])
        num_prisioneiros = int(entrada[idx+1])
        idx += 2
        
        tempo_minimo = 0
        tempo_maximo = 0
        
        for _ in range(num_prisioneiros):
            posicao = int(entrada[idx])
            idx += 1
            
            dist_min = min(posicao, comprimento_prancha - posicao)
            dist_max = max(posicao, comprimento_prancha - posicao)
            
            tempo_minimo = max(tempo_minimo, dist_min)
            tempo_maximo = max(tempo_maximo, dist_max)
            
        print(f"{tempo_minimo} {tempo_maximo}")

if __name__ == '__main__':
    prisioneiros()