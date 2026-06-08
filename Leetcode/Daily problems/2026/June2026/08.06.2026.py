class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans1 = []
        ans2 = []

        c = 0

        for i in nums:
            if i < pivot:
                ans1.append(i)
            elif i == pivot:
                c += 1
            else:
                ans2.append(i)

        for i in range(c):
            ans1.append(pivot)

        ans1 += ans2

        return ans1
