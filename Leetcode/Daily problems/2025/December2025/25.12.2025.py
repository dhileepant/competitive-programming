class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        i = 0
        ans = 0
        while k:
            t = max(0, happiness[i] - i)
            ans += t
            i += 1
            k -= 1
        return ans
