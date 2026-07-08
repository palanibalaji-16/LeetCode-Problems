class Solution:
    def minimumCost(self, co: List[int]) -> int:
        c=0
        s=0
        l=len(co)-1
        co.sort()
        while(l>=0):
            s=s+co[l]
            c=c+1
            l=l-1
            if c==2:
                c=0
                l=l-1
                continue
        return s

            
        
