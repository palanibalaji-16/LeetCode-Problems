class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=Counter(nums)
        for k,v in l.items():
            if(v>1):
                return k
        
