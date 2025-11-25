class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        r = 0
        for i in range(1,k+1):
            r = (r*10+1) % k
            if r == 0:
                return i
        return -1
        '''ans = -1
        for i in range(1,6123):
            n = '1' * i
            if int(n) % k == 0:
                ans = i
                break
        return ans'''
