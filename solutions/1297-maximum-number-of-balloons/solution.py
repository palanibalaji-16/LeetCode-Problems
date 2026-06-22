class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=text.count('b')
        o=text.count('o')
        a=text.count('a')
        n=text.count('n')
        l=text.count('l')
        c=0
        while b>=1 and o>=2 and a>=1 and l>=2 and n>=1:
              b=b-1
              o=o-2
              a=a-1
              n=n-1
              l=l-2
              c=c+1
        return c        
