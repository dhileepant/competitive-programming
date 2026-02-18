class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = str(bin(n)[2:])
        n = len(b)
        for i in range(n-1):
            if b[i] == b[i+1]:
                return False
        return True
