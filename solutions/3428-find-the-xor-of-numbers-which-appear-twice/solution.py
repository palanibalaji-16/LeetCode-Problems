from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        r=0
        c=Counter(nums)
        for k,v in c.items():
            if v==2:
                r=r^k
        return r
                       
        
