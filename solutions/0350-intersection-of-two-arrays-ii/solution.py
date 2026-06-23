class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i=0
        j=0
        l=[]
        nums1.sort()
        nums2.sort()
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                l.append(nums1[i])
                i=i+1
                j=j+1
            elif nums1[i]>=nums2[j]:
                j=j+1
            elif nums1[i]<=nums2[j]:
                i=i+1
            else:
                i=i+1
                j=j+1
        
        return l

