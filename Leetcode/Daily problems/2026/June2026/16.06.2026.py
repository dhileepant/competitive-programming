class Solution:
    def processStr(self, s: str) -> str:
        ans = ''
        for i in s:
            if i not in '*#%':
                ans += i
            elif i == '#':
                ans += ans
            elif i == '%':
                ans = ans[::-1]
            elif len(ans):
                ans = ans[:-1]
        return ans
