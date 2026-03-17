import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1[len(nums1):]=nums2
        nums1.sort()
        c=math.floor((len(nums1))/2)
        if (len(nums1))%2!=0:
            
            return  float(nums1[c])
        else:
            return  (nums1[c-1]+nums1[c])/2.0



        
