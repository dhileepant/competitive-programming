class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        s= sum(nums)
        l = 0
        ans = 0
        for i in range(len(nums)-1):
            l += nums[i]
            if (abs(l-(s-l)) & 1) == 0:
                ans += 1
        return ans
