class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev(s):
            return s[::-1]

        def inv(s):
            ans = ''
            for i in s:
                if i == '0':
                    ans += '1'
                else:
                    ans += '0'
            return ans

        s = '0'
        for i in range(n-1):
            s = s + '1' + rev(inv(s))
        return s[k-1]
