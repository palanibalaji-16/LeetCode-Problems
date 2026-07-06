class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        c=n[0]
        m=n[0]
        for i in n[1:]:
            c=max(i,c+i)
            m=max(c,m)
        
        return m

        
