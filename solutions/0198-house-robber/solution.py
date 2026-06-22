class Solution:
    def rob(self, nums: List[int]) -> int:
        l=0
        m=0
        for i in range(len(nums)):
            if(i%2==0):
                l=max(l+nums[i],m)
            else:
                m=max(m+nums[i],l)
        
        return max(l,m)
