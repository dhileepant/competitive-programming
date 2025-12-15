class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        c = 1
        p = prices[0]
        for i in range(1, len(prices)):
            if prices[i] == p-1:
                c += 1
            else:
                t = c * (c+1) // 2
                ans += t
                c = 1
            p = prices[i]
        ans += c * (c+1) // 2
        return ans
