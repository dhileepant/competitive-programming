class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = float('inf')
        n = len(arr)
        for i in range(n-1):
            mn = min(mn, arr[i+1]-arr[i])
        ans = []
        for i in range(n-1):
            a, b = arr[i], arr[i+1]
            if b-a == mn:
                ans.append([a, b])
        return ans
