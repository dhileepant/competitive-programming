class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        for i in str(n):
            s += int(i)
            p *= int(i)
        d = s+p
        if n%d == 0:
            return True 
        return False 
