class Solution:
    def differenceOfSum(self, n: List[int]) -> int:
        l=sum(n)
        s=0
        for i in n:
            while i!=0:
                b=i%10
                i=i//10
                s=s+b
            
        return l-s

        
