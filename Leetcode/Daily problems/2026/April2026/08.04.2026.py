class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            while l <= r:
                nums[l] = (nums[l]*v) % (1000000007)
                l += k
        ans = 0
        for i in nums:
            ans ^= i
        
        return ans
