class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)-1
        dna = [i for i in range(1,n+1)] + [n]
        
        return nums == dna
