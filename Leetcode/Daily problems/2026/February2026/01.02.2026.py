class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        d = nums[0]
        an = [nums[1],nums[2]]
        an.sort()
        for i in range(3,len(nums)):
            if an[1] > nums[i]:
                an[1] = nums[i]
                an.sort()
        return d + an[0] +an[1]
