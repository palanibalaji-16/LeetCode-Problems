class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n=len(s)
        d=k%n
        return s[d:]+s[:d]
