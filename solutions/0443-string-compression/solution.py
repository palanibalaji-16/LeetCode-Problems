class Solution:
    def compress(self, s: List[str]) -> int:
        i=0
        c=0
        k=0
        while(i<len(s)):
            w=s[i]
            c=0
            while i<len(s) and w==s[i]:
                c=c+1
                i=i+1
            s[k]=w
            k=k+1
            if c>1:
                for j in str(c):
                    s[k]=j
                    k=k+1
                
        return k



            


        
