class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        d =[]
        r = sum
        for i in range(num):
            t = min(r, 9)
            d.append(t)
            r -= t
        return ''.join(map(str,d))
