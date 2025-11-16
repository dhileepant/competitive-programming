class Solution:
    def numSub(self, s: str) -> int:
        c = 0
        ans = 0
        for i in s:
            if i == '1':
                c += 1
            else:
                res = (c * (c+1)) // 2
                ans += res
                ans = ans % (10**9 +7)
                c = 0
        if c:
            res = (c * (c+1)) // 2
            ans += res
            ans = ans % (10**9 +7)
        return ans
