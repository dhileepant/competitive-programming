class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        dna = 0
        for i in range(26):
            if chr(65+i) in word and chr(97+i) in word:
                dna += 1
        return dna
