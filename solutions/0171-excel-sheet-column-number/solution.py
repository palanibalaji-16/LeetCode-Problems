class Solution:
    def titleToNumber(self, co: str) -> int:
        c=0
        for i in co:
            c=c*26+(ord(i)-ord('A')+1)
        
        return c
        
