for t in range(int(input())):
    n = int(input())
    g = []
    x = 1
    for i in range(n):
        r = []
        for j in range(n):
            r.append(x)
            x += 1
        g.append(r)
    ans = 0
    for i in range(n):
        for j in range(n):
            s = g[i][j]
            if i > 0:
                s += g[i-1][j]
            if i+1 < n:
                s += g[i+1][j]
            if j > 0:
                s += g[i][j-1]
            if j+1 < n:
                s += g[i][j+1]
            # ans = max(ans , s)
            if s > ans:
                ans = s
    print(ans)
