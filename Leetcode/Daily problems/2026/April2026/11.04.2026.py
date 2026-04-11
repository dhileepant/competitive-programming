class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d={}
        r=float('inf')
        #ans = -1
        for i,x in enumerate(nums):
            if x not in d:d[x]=[]
            d[x].append(i)
        for v in d.values():
            if len(v)<3:continue
            for i in range(len(v)-2):
                a,b,c=v[i],v[i+1],v[i+2]
                r=min(r,abs(a-b)+abs(b-c)+abs(c-a))
        return -1 if r==float('inf') else r
        
