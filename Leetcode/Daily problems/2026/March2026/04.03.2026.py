class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        n = len(mat)
        m = len(mat[0])

        i = 0
        ans = 0

        while i < n:

            j = 0
            
            while j < m:

                if mat[i][j] == 1 and sum(mat[i]) == 1:

                    s = 0

                    for k in range(n):

                        s += mat[k][j]

                    if s == 1:
                        ans += 1
        

                j += 1

            
            i += 1


        return ans
