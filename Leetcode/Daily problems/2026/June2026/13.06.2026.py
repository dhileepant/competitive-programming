class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''
        for i in words:
            s = 0
            for j in i:
                s += weights[ord(j)-97]
            # print(s)
            n = s%26
            ans += chr(122-n)
        return ans
