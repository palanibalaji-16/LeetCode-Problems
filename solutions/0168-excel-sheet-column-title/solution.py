class Solution:
    def convertToTitle(self, n: int) -> str:
        l=[]
        while n>0:
            n=n-1
            cur=n%26
            n=int(n/26)
            g=chr(cur+ord('A'))
            l.append(g)
        
        b=l[::-1]
        
        return "".join(b) 

        
