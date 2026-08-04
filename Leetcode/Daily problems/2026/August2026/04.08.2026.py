class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        ans = []
        for i in range(min(nums), max(nums)):
            if i not in nums:
                ans.append(i)
        
        return ans
