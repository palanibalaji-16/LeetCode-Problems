class Solution:
    def mirrorDistance(self, n: int) -> int:
        p=str(n)
        c=p[::-1]
        b=int(c)
        return abs(n-b)
        
