class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c=set(nums)
        i=0
        while i in c:
            i+=1
        return i
        
