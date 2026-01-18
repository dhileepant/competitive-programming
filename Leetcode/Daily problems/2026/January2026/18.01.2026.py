class Solution:
    def largestMagicSquare(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        
        rs = [[0]*n for _ in range(m)]
        for i in range(m):
            rs[i][0] = g[i][0]
            for j in range(1, n):
                rs[i][j] = rs[i][j-1] + g[i][j]
        
        cs = [[0]*n for _ in range(m)]
        for j in range(n):
            cs[0][j] = g[0][j]
            for i in range(1, m):
                cs[i][j] = cs[i-1][j] + g[i][j]
        
        for e in range(min(m, n), 1, -1):
            for i in range(m - e + 1):
                for j in range(n - e + 1):
                    s = rs[i][j+e-1] - (0 if j == 0 else rs[i][j-1])
                    ok = True
                    
                    for x in range(i+1, i+e):
                        if rs[x][j+e-1] - (0 if j == 0 else rs[x][j-1]) != s:
                            ok = False
                            break
                    if not ok:
                        continue
                    
                    for y in range(j, j+e):
                        if cs[i+e-1][y] - (0 if i == 0 else cs[i-1][y]) != s:
                            ok = False
                            break
                    if not ok:
                        continue
                    
                    d1 = d2 = 0
                    for k in range(e):
                        d1 += g[i+k][j+k]
                        d2 += g[i+k][j+e-1-k]
                    
                    if d1 == s and d2 == s:
                        return e
        
        return 1
