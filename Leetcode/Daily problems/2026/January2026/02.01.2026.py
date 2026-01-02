class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # space complexity - O(1)
        for i in range(1,4):
            for j in range(len(nums) - i):
                if nums[j] == nums[i+j]:
                    return nums[j]
        # space complexity - O(n)
        # h = {}
        # for i in nums:
        #     if i in h:
        #         return i
        #     h[i] = 1
