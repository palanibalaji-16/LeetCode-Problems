class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        rem=0
        temp=x
        while(x):
            r=x%10
            rem=rem+r
            x=x//10

        if(temp%rem==0):
            return rem
        else:
            return -1

        
