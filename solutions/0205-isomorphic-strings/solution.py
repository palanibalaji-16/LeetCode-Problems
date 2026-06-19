class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l=set(zip(s,t))
        b=set(s)
        k=set(t)
        return len(l)==len(b)==len(k)
