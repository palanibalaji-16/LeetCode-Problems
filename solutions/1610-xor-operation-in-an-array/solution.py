class Solution:
    def xorOperation(self, n: int, s: int) -> int:
        p=0
        for i in range(n):
            p=p^(s+2*i)
        
        return p
        
