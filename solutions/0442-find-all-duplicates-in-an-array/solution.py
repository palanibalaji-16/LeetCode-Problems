from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=Counter(nums)
        j=[]
        for k,v in l.items():
            if(v>1):
                j.append(k)
        
        return j
        
