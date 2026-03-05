class Solution:
    def minOperations(self, s: str) -> int:
        a, n = 0, 0
        f, ff = 0, 1

        for i in s:
            if f:
                if i != '1':
                    a += 1
            else:
                if i != '0':
                    a += 1
            if ff:
                if i != '1':
                    n += 1
            else:
                if i != '0':
                    n += 1
            f = 1-f
            ff = 1-ff
        dna = min(a, n)
        return dna
