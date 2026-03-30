class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      n=list(s)
      b=list(t)
      if(len(n)!=len(b)):
        return False
      n.sort()
      b.sort()
      return n==b
