class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) % p == 0:
            return 0
        n = len(nums)
        s = 0
        for x in nums:
            s = (s + x) % p

        t = s % p
        if t == 0:
            return 0

        m = {0: -1}
        cs = 0
        res = n

        for i in range(n):
            cs = (cs + nums[i]) % p
            need = (cs - t + p) % p
            if need in m:
                res = min(res, i - m[need])
            m[cs] = i

        return -1 if res == n else res
