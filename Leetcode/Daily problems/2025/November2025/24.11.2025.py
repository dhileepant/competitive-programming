class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = [False] * len(nums)
        b = ''
        j = 0
        for i in nums:
            b += str(i)
            t = int(b, 2)
            if t % 5 == 0:
                ans [j] = True
            j += 1
        return ans
