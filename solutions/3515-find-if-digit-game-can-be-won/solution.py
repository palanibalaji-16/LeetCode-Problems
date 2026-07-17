class Solution:
    def canAliceWin(self, n: List[int]) -> bool:
        c=0
        p=0
        for i in n:
            if i<10:
                c=c+i
            else:
                p=p+i
            
        return c!=p
        
