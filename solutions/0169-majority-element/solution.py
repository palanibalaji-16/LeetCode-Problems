from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=Counter(nums)
        ma=-1
        m=-1
        for k,v in l.items():
            if v>ma:
                ma=v
                m=k
        return m

        
