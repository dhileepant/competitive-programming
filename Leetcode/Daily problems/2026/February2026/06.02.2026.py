class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        max_length = 0
        
        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            max_length = max(max_length, right - left + 1)
        
        return n - max_length
