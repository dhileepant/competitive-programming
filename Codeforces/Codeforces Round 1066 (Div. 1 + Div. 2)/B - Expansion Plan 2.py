for t in range(int(input())):
    n, x, y = map(int, input().split())
    s = input().strip()
    a = s.count('4')
    b = s.count('8')
    X = abs(x)
    Y = abs(y)
    dx = max(X - b, 0)
    dy = max(Y - b, 0)
    # f = 1 if dx + dy <= a else 0
    print("YES" if dx + dy <= a else "NO")
