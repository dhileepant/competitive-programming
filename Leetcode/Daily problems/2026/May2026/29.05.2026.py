class Solution:
    def minElement(self, nums: List[int]) -> int:
        dna = 234
        for i in nums:
            s = 0
            while i:
                s += (i%10)
                i //= 10
            if s < dna:
                dna = s
        return dna
