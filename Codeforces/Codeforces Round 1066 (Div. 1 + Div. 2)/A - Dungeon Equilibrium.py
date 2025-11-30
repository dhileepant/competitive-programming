for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = {}
    for x in a:
        f[x] = f.get(x, 0) + 1
    #c = Counter(a)
    ans = 0
    for v, c in f.items():
        if c < v:
            ans += c
        else:
            ans += c - v
    print(ans)
