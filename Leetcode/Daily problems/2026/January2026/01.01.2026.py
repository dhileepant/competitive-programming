class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = ''
        for i in digits:
            ans += str(i)
        ans = str(int(ans) + 1)
        l = []
        for i in ans:
            l.append(int(i))
        return l
