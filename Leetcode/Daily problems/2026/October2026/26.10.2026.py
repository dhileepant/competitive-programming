class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j,v,s):
            v[i][j] = 1
            s[0] += grid[i][j]
            for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                r = i + x
                c = j + y
                if 0 <= r < n and 0 <= c < m and not v[r][c] and grid[r][c] != 0:
                    dfs(r,c,v,s)
                    
        ans = 0
        v = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                s = [0]
                if not v[i][j]:
                    dfs(i,j,v,s)
                    if s[0]%k == 0:
                        ans += 1

        return ans
