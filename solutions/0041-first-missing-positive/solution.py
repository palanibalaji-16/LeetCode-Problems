
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        c=set(nums)
        i=1
        while i in c:
            i+=1
        return i
        
