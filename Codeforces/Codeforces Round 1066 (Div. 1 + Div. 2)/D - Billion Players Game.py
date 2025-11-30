for t in range(int(input())):
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    s1=0
    p=0
    ng=0
    e=0
    c=[]
    for v in a:
        if v<l:
            s1+=l-v
            p+=1
        elif v>l:
            s1+=v-l
            ng+=1
            c.append(v-l)
        else:
            e+=1
    d=p-ng
    if d>=0:
        ans1=s1
    else:
        d=-d
        if d<=e:
            ans1=s1
        else:
            d-=e
            c.sort()
            t=d
            k=t//2
            pref=0
            for i in range(k):
                pref+=c[i]
            cost=2*pref
            if t%2==1:
                cost+=c[k]
            ans1=s1-cost
    s2=0
    p=0
    ng=0
    e=0
    c=[]
    for v in a:
        if v<r:
            s2+=r-v
            p+=1
            c.append(r-v)
        elif v>r:
            s2+=v-r
            ng+=1
        else:
            e+=1
    d=p-ng
    if d<=0:
        ans2=s2
    else:
        if d<=e:
            ans2=s2
        else:
            d-=e
            c.sort()
            t=d
            k=t//2
            pref=0
            for i in range(k):
                pref+=c[i]
            cost=2*pref
            if t%2==1:
                cost+=c[k]
            ans2=s2-cost
    ans = max(ans1,ans2)
    # print(max(ans1,ans2))
    print(ans)
