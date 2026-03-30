class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        b=max(arr)
        return arr.index(b)
        
