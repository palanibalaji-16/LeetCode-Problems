class Solution:
    def reverseWords(self, s: str) -> str:
        p=s.split(" ")
        for i in range(len(p)):
            p[i]=p[i][::-1]
        
        return " ".join(p)
