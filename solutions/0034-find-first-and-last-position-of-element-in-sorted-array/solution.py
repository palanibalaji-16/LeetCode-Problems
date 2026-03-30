class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        i=0
        k=[]
        l=len(nums)-1
        while(i<=l):
            if(nums[i]==target):
                k.append(i)
            if i!=l and nums[l]==target :
                k.append(l)
    
            i=i+1
            l=l-1
        if not k:
            return [-1,-1]
        return [min(k),max(k)]
        
