class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c=0
        for i in nums:
            while(i>0):
                b=i%10
                i=i//10
                if b==digit:
                    c=c+1
        
        return c
        
