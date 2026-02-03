class Solution:
   def isTrionic(self, nums: List[int]) -> bool:
    n = len(nums)
    for p in range(1, n - 2):
        inc1 = all(nums[i] < nums[i + 1] for i in range(p))
        if not inc1:
            continue
        for q in range(p + 1, n - 1):
            dec = all(nums[i] > nums[i + 1] for i in range(p, q))
            inc2 = all(nums[i] < nums[i + 1] for i in range(q, n - 1))
            if dec and inc2:
                return True
    return False
