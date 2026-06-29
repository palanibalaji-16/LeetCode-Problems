class Solution:
    def detectCapitalUse(self, w: str) -> bool:
        if w.isupper() or w.islower() or w.istitle():
            return True
        return False
        
