class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        v=Counter(nums)
        for k,v in v.items():
            if v==1:
                b=k


        return b
        
