class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        open = 0
        for i in s:
            if i == "(":
                if open > 0:
                    ans.append(i)
                open += 1
            else:
                if open > 1:
                    ans.append(i)
                open -= 1
        return ''.join(ans)
