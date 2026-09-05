class Solution:
    def firstStableIndex(self, d: list[int], k: int) -> int:
        n=len(d)
        s=[0]*n
        s[-1]=d[-1]
        for i in range(n-2,-1,-1):
            s[i]=min(s[i+1],d[i])
        m=-10**17 +34
        for i in range(n):
            if d[i]>m:
                m=d[i]
            if m-s[i]<=k:
                return i
        return -1
