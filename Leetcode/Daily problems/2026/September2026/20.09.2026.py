class Solution:
    def reverseDegree(self, s: str) -> int:
        dn = 0
        i = 1 
        for j in s:
            dn += (((ord('z')+1)-ord(j)) * i)
            i += 1
        return dn
