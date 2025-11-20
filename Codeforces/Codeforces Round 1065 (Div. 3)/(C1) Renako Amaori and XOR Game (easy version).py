for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=y=0
    for i in a:x^=i
    for i in b:y^=i
    if x==y:
        print("Tie")
        continue
    # ans  =0
    for i in range(n-1,-1,-1):
        if a[i]!=b[i]:
            print("Ajisai" if (i+1)%2 else "Mai")
            break
