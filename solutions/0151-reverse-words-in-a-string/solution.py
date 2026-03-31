class Solution:
    def reverseWords(self, s: str) -> str:
        p=s.split()
        c=p[::-1]
        h=" ".join(c)
        return h



        
