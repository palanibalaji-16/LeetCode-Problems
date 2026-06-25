class Solution:
    def countDigits(self, n: int) -> int:
        t=False
        c=0
        o=n
        while(n!=0):
            b=n%10
            n=n//10
            if o%b==0:
                t=True
                c=c+1
            
        if(t):
            return c
        else:
            return c
            
        
