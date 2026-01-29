class Solution:
    def minimumCost(self, s, t, o, c, w):
        r = 0
        inf = 10**18
        d = [[inf]*26 for _ in range(26)]

        for x,y,z in zip(o,c,w):
            i = ord(x) - 97
            j = ord(y) - 97

            if z < d[i][j]:
                d[i][j] = z

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    
                    v = d[i][k] + d[k][j]

                    if v < d[i][j]:
                        d[i][j] = v

        for x,y in zip(s,t):
            if x == y:
                continue
            i = ord(x) - 97
            j = ord(y) - 97

            if d[i][j] >= inf:
                return -1
            r += d[i][j]

        return r
