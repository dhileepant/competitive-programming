class Solution:
    def validateCoupons(self, code: List[str], bl: List[str], a: List[bool]) -> List[str]:
        v = ['electronics', 'grocery', 'pharmacy', 'restaurant']
        co = {ct : i for i,ct in enumerate(v)}
        g = [[] for i in range(4)]
        for i in range(len(a)):
            if not a[i] or bl[i] not in co or not code[i]:
                continue
            if all(c.isalnum() or c=='_' for c in code[i]):
                ind = co[bl[i]]
                g[ind].append(code[i])
        ans = []
        for i in g:
            i.sort()
            ans.extend(i)

        return ans
