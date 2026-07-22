class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        b=0
        while n>0:
            b=b+n%10
            n=n//10
        return b
    
        
