class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        b=s.split()
        if len(b)!=len(p):
            return False
        
        return len(set(b))==len(set(p))==len(set(zip(b,p)))
