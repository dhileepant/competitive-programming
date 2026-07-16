class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        g = []
        cur = -1
        
        for x132 in nums:
            cur = max(cur, x132)
            g.append(math.gcd(x132, cur))
        
        g.sort()
        
        l = 0
        r = n - 1
        res = 0
        
        while l < r:
            val = math.gcd(g[l], g[r])
            res += val
            l += 1
            r -= 1
        
        return res
