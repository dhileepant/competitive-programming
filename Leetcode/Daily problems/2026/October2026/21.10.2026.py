class Solution:
    def minOperations(self, s: str) -> int:
        t = "".join(sorted(s))
        n = len(s)
        
        if s == t:
            return 0
        
        if n == 2:
            return -1
        
        if s[0] == t[0] or s[-1] == t[-1]:
            return 1
        
        mx = t[-1]
        mn = t[0]
        
        if s[0] == mx and s.count(mx) == 1 and s[-1] == mn and s.count(mn) == 1:
            return 3
        
        return 2
