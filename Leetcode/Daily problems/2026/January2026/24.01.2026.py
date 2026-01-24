class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = []
        nums.sort()
        for i in range(len(nums) // 2):
            ans.append(nums[i] + nums[-(i+1)])
        return max(ans)
