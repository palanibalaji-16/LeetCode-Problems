class Solution:
    def sortColors(self, n: List[int]) -> None:
        l=0
        m=0
        h=len(n)-1
        while(h>=m):
            if n[m]==0:
                t=n[l]
                n[l]=n[m]
                n[m]=t
                m=m+1
                l=l+1
            elif n[m]==1:
                m=m+1
            else:
                t=n[m]
                n[m]=n[h]
                n[h]=t
                h=h-1
            
        
        
