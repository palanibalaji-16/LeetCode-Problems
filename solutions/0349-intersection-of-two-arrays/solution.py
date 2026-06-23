class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        b=set(nums1)
        n=set(nums2)
        d=b&n
        return list(d)
        
