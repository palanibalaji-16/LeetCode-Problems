class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        c=10
        f=9
        o=9
        for i in range(1,n):
            f=f*o
            c=c+f
            o=o-1
        return c
        
