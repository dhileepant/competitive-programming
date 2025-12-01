class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # return sum(batteries) // n
        l, r = 1, sum(batteries) // n   
        while l < r:
            m = (l+r) // 2 + 1      
            e = 0
            for i in batteries:
                e += min(i, m)          
            if e//n >= m:
                l = m
            else:
                r = m-1       
        return l
