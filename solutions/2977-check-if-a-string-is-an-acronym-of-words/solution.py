class Solution:
    def isAcronym(self, w: List[str], s: str) -> bool:
        if len(w)!=len(s):
            return False
        for i in range(len(s)):
            if w[i][0]!=s[i]:
                return False
        return True

        
