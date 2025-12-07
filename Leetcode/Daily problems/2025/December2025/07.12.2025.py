class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        if (low&1) == 1 or (high&1) == 1:
            ans += 1
        d = high - low
        ans += (d//2)
        return ans
