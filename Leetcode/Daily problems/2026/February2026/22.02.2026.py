class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        ans = 0
        c = 1
        if b.count('1') < 2:
            return 0
        for i in b:
            if i == '1':
                ans = max(ans, c)
                c = 1
            else:
                c += 1
        return ans
