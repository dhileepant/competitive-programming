class Solution:
    def maxProfit(self, p, s, k):
        n=len(p)
        u=[0]*(n+1)
        v=[0]*(n+1)
        for i in range(n):
            u[i+1]=u[i]+s[i]*p[i]
            v[i+1]=v[i]+p[i]
        x=u[n]
        g=0
        h=k//2
        for i in range(n-k+1):
            j=i+k
            m=i+h
            w=(v[j]-v[m])-(u[j]-u[i])
            if w>g:g=w
        return x+g
