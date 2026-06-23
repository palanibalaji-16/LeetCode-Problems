class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=max(arr)
        for i in range(len(arr)):
            if l==arr[i]:
                return i
        
