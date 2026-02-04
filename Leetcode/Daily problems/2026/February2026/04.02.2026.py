class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")
        i132 = 0
        while i132 < n:
            j = i132 + 1
            res = 0
            while j < n and nums[j - 1] < nums[j]:
                j += 1
            p = j - 1
            if p == i132:
                i132 += 1
                continue
            res += nums[p] + nums[p - 1]
            while j < n and nums[j - 1] > nums[j]:
                res += nums[j]
                j += 1
            q = j - 1
            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i132 = q
                continue
            res += nums[q + 1]
            mx = 0
            cur = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                cur += nums[k]
                if cur > mx:
                    mx = cur
                k += 1
            res += mx
            mx = 0
            cur = 0
            for k in range(p - 2, i132 - 1, -1):
                cur += nums[k]
                if cur > mx:
                    mx = cur
            res += mx
            if res > ans:
                ans = res
            i132 = q
        return ans
