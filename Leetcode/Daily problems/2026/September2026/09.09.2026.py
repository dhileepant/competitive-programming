class Solution:
    def countCommas(self, nd: int) -> int:
        dn = 0
        p = 1000
        
        while p <= nd:
            dn += nd - p + 1
            p *= 1000
        
        return dn
