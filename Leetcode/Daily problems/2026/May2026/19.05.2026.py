class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        q = len(nums2)
        d, a = 0, 0
        while d < n and a < q:
            if nums1[d] == nums2[a]:
                return nums1[d]
            if nums1[d] > nums2[a]:
                a += 1
            else:
                d += 1
        return -1
