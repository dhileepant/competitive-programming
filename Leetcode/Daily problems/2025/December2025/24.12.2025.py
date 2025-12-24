class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApples = sum(apple)
        capacity.sort(reverse = True)
        ans  = 0
        for i in capacity:
            ans += 1
            totalApples -= i
            if totalApples < 1:
                break
        return ans
