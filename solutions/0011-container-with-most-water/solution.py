class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        m=0
        while(l<r):
            d=r-l
            ch=min(h[l],h[r])
            cw=d*ch
            m=max(m,cw)
            if h[l]<h[r]:
                l=l+1
            else:
                r=r-1
        return m
        
