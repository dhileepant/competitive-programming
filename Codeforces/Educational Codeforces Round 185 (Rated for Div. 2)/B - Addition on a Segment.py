for t in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    s = sum(b)
    z = 0
    for v in b:
        if v == 0:
            z += 1
    # ans = min(n - z, s - n + 1)
    print(min(n - z, s - n + 1))
