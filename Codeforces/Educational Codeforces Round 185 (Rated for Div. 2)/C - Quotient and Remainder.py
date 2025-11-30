for t in range(int(input())):
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    q.sort()
    b = []
    # ans = 0
    if k >= 2:
        for x in r:
            if x > k - 2:
                continue
            y = (k - x) // (x + 1)
            if y > 0:
                b.append(y)
    b.sort()
    i = 0
    m = len(q)
    ans = 0
    for y in b:
        if i >= m:
            break
        if q[i] <= y:
            ans += 1
            i += 1
    print(ans)
