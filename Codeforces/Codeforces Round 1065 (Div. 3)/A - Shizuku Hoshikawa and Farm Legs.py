for t in range(int(input())):
    n = int(input())
    # ans = n // 4 + 1
    print(0 if n % 2 else n // 4 + 1)
