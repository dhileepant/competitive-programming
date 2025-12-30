class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0
        ans = 0
        i = 0
        while i < n-2:
            j = 0
            while j < m-2:
                a = []
                for k in range(i,i+3):
                    for t in range(j, j+3):
                        a.append(grid[k][t])
                j += 1
                l = a[::]
                a.sort()
                if a != [1,2,3,4,5,6,7,8,9]:
                    continue
                print(l)
                if l[0]+l[1]+l[2] == l[3]+l[4]+l[5] == l[6]+l[7]+l[8] == l[0]+l[3]+l[6] == l[1]+l[4]+l[7] == l[2]+l[5]+l[8] == l[0]+l[4]+l[8] == l[2]+l[4]+l[6]:
                    ans += 1
            i += 1
        return ans
