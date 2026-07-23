class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        m=0
        r=len(h)-1
        while l<r:
            m=max(m,min(h[l],h[r])*(r-l))
            if h[l]<h[r]:
                l=l+1
            else:
                r=r-1
        return m
        
