class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        curr = 0
        ans = []
        for i in nums:
            ans.append(abs(s - (curr*2+i)))
            curr += i
        return ans
