class Solution:
    def earliestFinishTime(self, ls: list[int], ld: list[int], ws: list[int], wd: list[int]) -> int:
        ans = float('inf')
        for i in range(len(ls)):
            for j in range(len(ws)):
                a = ls[i] + ld[i]
                b = max(ws[j], a) + wd[j]
                ans = min(ans, b)
                a = ws[j] + wd[j]
                b = max(ls[i], a) + ld[i]
                ans = min(ans, b)
        return ans
