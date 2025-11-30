from collections import Counter

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    co = 0
    ce = 0
    
    for v in c.values():
        if v % 2 == 1:
            co += 1
        else:
            ce += 1

    best = 0
    for t2 in range(ce, -1, -1):
        L = max(0, co + t2 - n)
        U = min(co, n - t2)
        
        if L > U:
            continue
        
        need = (n - t2) & 1
        x = L if (L & 1) == need else L + 1
        
        if x <= U:
            best = t2
            break

    # ans = 4 * co
    ans = co + 2 * best
    print(ans)
