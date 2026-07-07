class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        for i in str(n):
            if i!='0':
                x += i
        if not x:
            return 0
        s = sum(list(map(int, x)))
        ans = int(x) * s
        return ans
