class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(n):
            cnt = 0
            s = 0
            for i in range(1,int(sqrt(n))+1):
                if n%i == 0:
                    cnt += 1
                    s += i
                    if n//i != i:
                        cnt += 1
                        s += (n//i)
                if cnt > 4:
                    return 0
            if cnt == 4:
                return s
            return 0
        
        ans = 0
        for i in nums:
            ans += divisors(i)
        return ans
