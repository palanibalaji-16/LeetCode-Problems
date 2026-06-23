class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        b=set(nums1)
        c=set(nums2)
        d=b&c
        return min(d,default=-1)

        
