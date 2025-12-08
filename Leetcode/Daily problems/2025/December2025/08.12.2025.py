class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n):
            for j in range(i+1,n + 1):
                c = int(sqrt(i**2 + j*j + 1))
                if c <= n and c*c == i*i + j*j:
                    ans += 2
        return ans
        '''ans = 0
        for i in range(1,n-1):
            for j in range(i+1,n):
                for k in range(j+1,n+1):
                    if i*i + j*j == k*k:
                        ans += 2
                        print(i,j,k)
        return ans'''
