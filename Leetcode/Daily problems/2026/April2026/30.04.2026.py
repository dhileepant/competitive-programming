class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[-1] * (k + 1) for i in range(m)] for j in range(n)]
        iv = 2 if grid[0][0] == 2 else (1 if grid[0][0] == 1 else 0)
        icnt = 1 if grid[0][0] > 0 else 0
        dp[0][0][icnt] = iv
        for r in range(n):
            for c in range(m):
                for kk in range(k + 1):
                    if dp[r][c][kk] == -1:
                        continue
                    for dr, dc in ((1, 0), (0, 1)):
                        nr, nc = r + dr, c + dc
                        if nr >= n or nc >= m:
                            continue
                        a = 1 if grid[nr][nc] > 0 else 0
                        x = kk + a
                        if x > k:
                            continue
                        y = 2 if grid[nr][nc] == 2 else (1 if grid[nr][nc] == 1 else 0)
                        dp[nr][nc][x] = max(dp[nr][nc][x], dp[r][c][kk] + y)
        return max(dp[n - 1][m - 1])
        
        '''n,m=len(grid),len(grid[0])
        p=[[-1]*(k+1) for i in range(m)]
        curr=[[-1]*(k+1) for i in range(m)]
        iv=2 if grid[0][0]==2 else (1 if grid[0][0]==1 else 0)
        icnt=1 if grid[0][0]>0 else 0
        p[0][icnt]=iv
        for i in range(n):
            for c in range(m):
                for k in range(k+1):
                    if (i>0 and p[c][k]!=-1) or (c>0 and curr[c-1][k]!=-1):
                        b=max(p[c][k],curr[c-1][k])
                        a=1 if grid[i][c]>0 else 0
                        x=k+a
                        if x<=k:
                            y=2 if grid[i][c]==2 else (1 if grid[i][c]==1 else 0)
                            curr[c][x]=max(curr[c][x],b+y)
            p,curr=curr,[[-1]*(k+1) for i in range(m)]
        ans = max(p[-1])
        return ans #max(p[-1])'''
