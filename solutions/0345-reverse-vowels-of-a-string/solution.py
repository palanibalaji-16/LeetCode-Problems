class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        v="AaEeIiOoUu"
        a=list(s)
        while i<j:
            if a[i] in v and a[j] in v:
                a[i],a[j]=a[j],a[i]
                i=i+1
                j=j-1
            elif a[i] in v and a[j] not in v:
                j=j-1
            elif a[i] not in v and a[j] in v:
                i=i+1
            else:
                i=i+1
                j=j-1
            
        return "".join(a)
