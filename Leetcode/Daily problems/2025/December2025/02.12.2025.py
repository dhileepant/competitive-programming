class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        pn = defaultdict(int)
        mod = 10**9 + 7
        ans, ts = 0, 0
        for i in points:
            pn[i[1]] += 1
        for i in pn.values():
            e = i * (i - 1) // 2
            ans = (ans + e * ts) % mod
            ts = (ts + e) % mod
        return ans
