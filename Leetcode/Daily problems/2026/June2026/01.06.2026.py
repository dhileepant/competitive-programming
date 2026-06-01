class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        c = 0
        ans = 0
        
        for i in cost:
            if c == 2:
                c = 0
                continue
            c += 1
            ans += i

        return ans
