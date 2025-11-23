class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -float("inf"), -float("inf")]
        for num in nums:
            g = f[:]
            for i in range(3):
                g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            f = g
        return f[0]
        '''a,b,c = [], [], []
        for i in nums:
            if i%3 == 0:
                a.append(i)
            elif i%3 == 1:
                b.append(i)
            else:
                c.append(i)
        ans = sum(a)
        n = min(len())'''
