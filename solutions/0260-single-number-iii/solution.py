from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d=[]
        c=Counter(nums)
        for k,v in c.items():
            if v==1:
                d.append(k)
            
        return d
