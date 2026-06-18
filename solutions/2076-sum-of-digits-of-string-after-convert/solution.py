class Solution:
    def getLucky(self, s: str, k: int) -> int:
        b="abcdefghijklmnopqrstuvwxyz"
        c=""
       
        for i in range(len(s)):
            o=b.index(s[i])+1
            c=c+str(o)
        
        for j in range(k):
                v=0
                for i in range(len(c)):
                    v=v+int(c[i])
                c=str(v)
        return v



        
