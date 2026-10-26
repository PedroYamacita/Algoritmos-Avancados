import sys
import heapq

def main():
    t = sys.stdin.read().split()
    i = 0
    while i < len(t):
        n = int(t[i]); i += 1
        nomes = t[i:i + n]; i += n
        m = int(t[i]); i += 1
        adj = {b: [] for b in nomes}
        grau = {b: 0 for b in nomes}
        for _ in range(m):
            a, b = t[i], t[i + 1]; i += 2
            adj[a].append(b)
            grau[b] += 1
        heap = [b for b in nomes if grau[b] == 0]
        heapq.heapify(heap)
        ordem = []
        while heap:
            u = heapq.heappop(heap)
            ordem.append(u)
            for v in adj[u]:
                grau[v] -= 1
                if grau[v] == 0:
                    heapq.heappush(heap, v)
        print(" ".join(ordem) + ".")

main()