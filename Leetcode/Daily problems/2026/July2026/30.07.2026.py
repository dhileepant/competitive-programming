class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word).most_common()
        curr = 2
        p = 1
        ans = 0
        print(c)
        for j,i in c:
            ans += (p * i)
            if curr == 9:
                curr = 1
                p += 1
            curr += 1
        return ans
