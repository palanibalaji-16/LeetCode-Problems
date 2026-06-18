class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            c=0
            while(n!=0):
                b=n%10
                c=c+b**2
                n=n//10
            n=c
        
        if(n==1):
            return True
        else:
            return False       
