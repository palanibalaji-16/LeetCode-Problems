class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        b=max(nums)
        return nums.index(b)

        
