class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        a = ''
        for i in b:
            if i == '1':
                a += '0'
            else:
                a += '1'

        return int(a, 2)
