import sys
from bisect import bisect_left, bisect_right

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    it = iter(input)
    
    try:
        T = int(next(it))
    except StopIteration:
        return
        
    for _ in range(T):
        P = int(next(it))
        C = int(next(it))
        
        A = []
        for _ in range(P):
            A.append(int(next(it)))
            
        C_list = []
        for _ in range(C):
            C_list.append(int(next(it)))
            
        A.sort()
        C_list.sort()
        
        candidates = set([0])
        candidates.update(A)
        candidates.update(C_list)
        
        sorted_candidates = sorted(list(candidates))
        
        min_angry = float('inf')
        best_price = -1
        
        for x in sorted_candidates:
            adv_angry = P - bisect_right(A, x)
            
            cust_angry = bisect_left(C_list, x)
            
            total_angry = adv_angry + cust_angry
            
            if total_angry < min_angry:
                min_angry = total_angry
                best_price = x
                
        print(f"{best_price} {min_angry}")

if __name__ == '__main__':
    solve()