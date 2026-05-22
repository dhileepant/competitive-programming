class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        k = 0
        s, e = 0, n-1               
        while s <= e:
            m = (s+e) // 2
            if nums[m] >= nums[0]:
                s = m+1
            else:
                k = m 
                e = m-1

        s, e = 0, n-1
        while s <= e:
            m = (s+e) // 2
            if nums[(m+k)%n] == target:
                return (m+k)%n
            elif nums[(m+k)%n] > target:
                e = m-1
            else:
                s = m+1

        # if target in nums:
        #     return nums.index(target)
        return -1
