class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pre=[0]*n
        suf=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i])
        suf[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suf[i]=min(suf[i+1],nums[i])
        for i132 in range(n):
            if pre[i132]-suf[i132]<=k:
                return i132
        return -1
