import sys

def resolver():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n_testes_str = next(iterator)
        n_testes = int(n_testes_str)
    except StopIteration:
        return
        
    if n_testes < 1 or n_testes > 5:
        return
        
    for _ in range(n_testes):
        try:
            n_cores = int(next(iterator))
        except StopIteration:
            break
            
        if n_cores < 3 or n_cores > 12:
            return
            
        cores = {}
        cores_string = []
        
        for preferencia in range(n_cores):
            cor = next(iterator)
            cores[cor] = preferencia
            cores_string.append(cor)
            
        n_par = int(next(iterator))
        
        par_proibido = [[False] * n_cores for _ in range(n_cores)]
        
        for _ in range(n_par):
            cor1 = next(iterator)
            cor2 = next(iterator)
            if cor1 in cores and cor2 in cores:
                idx1 = cores[cor1]
                idx2 = cores[cor2]
                par_proibido[idx1][idx2] = True
                par_proibido[idx2][idx1] = True
                
        quantidade_pinturas = 0
        melhor_pintura = []
        encontrou_melhor = False
        cores_usadas = [False] * n_cores
        pintura_atual = []
        
        # Função recursiva de backtracking
        def pintar(posicao):
            nonlocal quantidade_pinturas, melhor_pintura, encontrou_melhor
            
            # Se a posição atual for igual ao número de cores, finalizou a pintura
            if posicao == n_cores:
                quantidade_pinturas += 1
                
                # Verifica se é a pintura favorita
                if not encontrou_melhor or pintura_atual < melhor_pintura:
                    melhor_pintura = list(pintura_atual) 
                    encontrou_melhor = True
                return
            
            # Tenta pintar a faixa atual com as cores disponíveis
            for i in range(n_cores):
                # Verifica se a cor já foi usada
                if cores_usadas[i]:
                    continue
                # Verifica se a cor forma um par proibido com a anterior
                if posicao != 0 and par_proibido[pintura_atual[-1]][i]:
                    continue
                    
                # Pinta com a cor escolhida
                pintura_atual.append(i)
                cores_usadas[i] = True
                
                pintar(posicao + 1)
                
                pintura_atual.pop()
                cores_usadas[i] = False
                
        pintar(0)
        
        print(quantidade_pinturas)
        print(" ".join(cores_string[idx] for idx in melhor_pintura))

if __name__ == '__main__':
    resolver()