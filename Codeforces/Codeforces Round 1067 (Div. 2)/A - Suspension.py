for t in range(int(input())):
    n = int(input())
    y, r = map(int,input().split())
    ans = min(n, r + (y//2))
    print(ans)
