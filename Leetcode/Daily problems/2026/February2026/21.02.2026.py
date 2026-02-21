class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(n):
            if n<2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    return False
            return True
            
        ans = 0
        for i in range(left, right+1):
            b = bin(i)[2:]
            o = b.count('1')
            if isprime(o):
                ans += 1
        return ans
