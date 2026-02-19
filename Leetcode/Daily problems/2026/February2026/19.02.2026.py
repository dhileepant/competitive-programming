class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
        # n = len(s)
        # ans = 0
        # i = 0

        # while i < n:
        #     o, z = 0, 0
        #     j = i
        #     m = 0

        #     if s[i] == '1':
        #         while j < n and s[j] == '1':
        #             o += 1
        #             j += 1
        #         m = j
        #         while j < n and s[j] == '0' and z < o:
        #             z += 1
        #             j += 1
        #     else:
        #         while j < n and s[j] == '0':
        #             z += 1
        #             j += 1
        #         m = j
        #         while j < n and s[j] == '1' and o < z:
        #             o += 1
        #             j += 1
        #     if o == z:
        #         ans += o
        #         i = m
        #     else:
        #         i += 1

        # return ans
