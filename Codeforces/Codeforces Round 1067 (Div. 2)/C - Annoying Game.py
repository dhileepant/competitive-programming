for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # i = 0
    inf = 10**17

    le = [0] * n
    pl = [0] * n
    for i in range(n):
        if i == 0:
            le[i] = a[i]
        else:
            le[i] = max(a[i], a[i] + le[i - 1])
        if i == 0:
            pl[i] = le[i]
        else:
            pl[i] = max(pl[i - 1], le[i])

    ri = [0] * n
    pr = [0] * n
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            ri[i] = a[i]
        else:
            ri[i] = max(a[i], a[i] + ri[i + 1])
        if i == n - 1:
            pr[i] = ri[i]
        else:
            pr[i] = max(pr[i + 1], ri[i])

    base = pl[-1]

    if k % 2 == 0:
        print(base)
        continue
    # ans = -1
    ans = -inf
    for i in range(n):
        w = -inf
        if i > 0:
            w = pl[i - 1]
        if i < n - 1:
            if pr[i + 1] > w:
                w = pr[i + 1]

        con = le[i] + ri[i] - a[i]
        p = max(w, con + b[i])
        m = max(w, con - b[i])

        if p > ans:
            ans = p
        if m > ans:
            ans = m

    print(ans)
