class Solution:
    def defangIPaddr(self, a: str) -> str:
        l=[]
        for i in a:
            if i.isdigit():
                l.append(i)
            elif i==".":
                l.append("[.]")
            
        return "".join(l)
        
