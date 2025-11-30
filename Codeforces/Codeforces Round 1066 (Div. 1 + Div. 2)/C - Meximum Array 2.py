for t in range(int(input())):
    n,k,q=map(int,input().split())
    t1=[0]*n
    t2=[0]*n
    s1=[]
    s2=[]
    for i in range(q):
        c,l,r=map(int,input().split())
        l-=1;r-=1
        if c==1:
            s1.append((l,r))
            for i in range(l,r+1):
                t1[i]=1
        else:
            s2.append((l,r))
            for i in range(l,r+1):
                t2[i]=1
    a=[-1]*n
    kp=k+1
    for i in range(n):
        if t1[i] and t2[i]:
            a[i]=kp
    f=[]
    for i in range(n):
        if not t1[i]:
            f.append(i)
    if k>0:
        for j,i in enumerate(f):
            a[i]=j%k
    for l,r in s1:
        for i in range(l,r+1):
            if not t2[i]:
                a[i]=k
                break
    for i in range(n):
        if a[i]==-1 and t1[i]:
            a[i]=kp
        if a[i]==-1:
            a[i]=0
    print(*a)
    # print()
