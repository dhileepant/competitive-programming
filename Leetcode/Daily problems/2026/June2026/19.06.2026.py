class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        p = 0
        ans = 0
        for i in gain:
            ans = max(ans, i+p)
            p = i+p
            # print(ans, p)
        return ans
