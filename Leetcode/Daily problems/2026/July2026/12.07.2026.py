class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dn = sorted(set(arr))
        nd = {}
        for i,j in enumerate(dn):
            nd[j] = i+1
        return [nd[i] for i in arr]
