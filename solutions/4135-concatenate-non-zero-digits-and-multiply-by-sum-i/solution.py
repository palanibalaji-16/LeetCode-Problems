class Solution:
    def sumAndMultiply(self, n: int) -> int:
        b=str(n)
        l=[]
        su=0
        for i in b:
            if int(i)!=0:
                su=su+int(i)
                l.append(i)  
        if not l:
            return 0 
        p="".join(l)
        return int(p)*su
   



