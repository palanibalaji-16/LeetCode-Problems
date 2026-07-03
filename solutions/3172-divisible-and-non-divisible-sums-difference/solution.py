class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        c,b=0,0
        for i in range(1,n+1):
            if i%m==0:
                c=c+i
            else:
                b=b+i
        return b-c
            
                
        
