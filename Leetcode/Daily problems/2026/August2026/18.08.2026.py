class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        if k == 1:
            c = Counter(nums)
            dn = [i for i,j in c.items() if j == 1]
            if dn:  return max(dn)
            return -1
        f = nums.count(nums[0])
        l = nums.count(nums[-1])
        if (nums[0] > nums[-1] or l > 1) and f == 1:
            return nums[0]
        if (nums[0] < nums[-1] or f > 1) and l == 1:
            return nums[-1]
        return -1
