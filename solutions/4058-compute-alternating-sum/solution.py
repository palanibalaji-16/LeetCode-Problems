class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
       
        nums1=0
        for i in range(0,len(nums)):
            if(i%2==0):
                nums1=nums1+nums[i]

            else:
                nums1=nums1-nums[i]
        
        return nums1
