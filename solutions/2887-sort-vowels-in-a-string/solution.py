class Solution:
    def sortVowels(self, s: str) -> str:
        v=[]
        j=0
        f=""
        for i in s:
            if i in "AaEeIiOoUu":
                v.append(i)
        
        v.sort()
        for i in s:
            if i in "AaEeIiOoUu":
                f=f+v[j]
                j=j+1
            else:
                f=f+i
        
        return f
        
