class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        o, f = 0, 1
        for i in s:
            if i == '0':
                f = 0
            else:
                if not f:
                    return False
                  
        return True
