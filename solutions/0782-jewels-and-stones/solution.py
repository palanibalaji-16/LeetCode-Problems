class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        c=0
        for i in j:
            c=c+s.count(i)
            
        return c
        
