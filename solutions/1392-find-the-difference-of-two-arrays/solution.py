class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[]
        a=set(nums1)
        b=set(nums2)
        n=a-b
        o=b-a
        l.append(list(n))
        l.append(list(o))
        return l

        
