class Solution:
    def capitalizeTitle(self, t: str) -> str:
        s=t.split()
        p=""
        l=[]
        for i in s:
            if len(i)>2:
                p=i[0].upper()+i[1:].lower()
                l.append(p)
            else:
                l.append(i.lower())
        return " ".join(l)
        
