class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            if nums[i] != 0:
                dna = nums[i]%n
                ans[i] = nums[(i+dna)%n]
            else:
                ans[i] = nums[i]
        return ans
