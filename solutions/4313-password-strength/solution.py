class Solution:
    def passwordStrength(self, p: str) -> int:
        res=0
        k=set(p)
        for j in k:
            if j.islower():
                res=res+1
            elif j.isupper():
                res=res+2
            elif j.isdigit():
                res=res+3
            elif not j.isalnum():
                res=res+5
            
        return res

        
