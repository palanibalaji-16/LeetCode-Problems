class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        su=0
        while(n!=0):
            b=n%10
            n=n//10
            p=p*b
            su=su+b
        return p-su
        
