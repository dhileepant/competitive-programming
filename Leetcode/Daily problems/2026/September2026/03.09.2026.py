class Solution:
    def uniformArray(self, c):
        m = min(c)
        if (m & 1):
            return True
        for dn in c:
            if dn % 2:
                return False
        return True
