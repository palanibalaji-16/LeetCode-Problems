class Solution:
    def findComplement(self, n: int) -> int:
        b=bin(n)[2:]
        s=[]
        for i in b:
            if i=="0":
                s.append("1")
            else:
                s.append("0")
            
        u="".join(s)
        return int(u,2)
        
