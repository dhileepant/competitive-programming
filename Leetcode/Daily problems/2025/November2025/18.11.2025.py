class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
        '''if len(bits) == 1 or (bits[-1] == 0 and bits[-2] == 0) or ((len(bits)&1) == 1 and bits[-1] == 0 and bits[-3] != 0):
            return True
        if len(bits) > 3 and bits[-1] == 0 and bits[-2] == 1 
        return False'''
