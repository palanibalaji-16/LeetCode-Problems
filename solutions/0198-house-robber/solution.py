class Solution:
    def rob(self, n: List[int]) -> int:
        l=0
        m=0
        k=0
        for i in n:
            l=i+m
            m=k
            k=max(k,l)


        return k
        
