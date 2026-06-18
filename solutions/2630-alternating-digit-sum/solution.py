class Solution:
    def alternateDigitSum(self, n: int) -> int:
        p=0
        s=str(n)
        for i in range(len(s)):
            d=int(s[i])
            if i%2==0:
                p=p+d
            else:
                p=p-d
        
        return p
