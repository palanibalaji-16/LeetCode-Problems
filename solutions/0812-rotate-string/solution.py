class Solution:
    def rotateString(self, s: str, g: str) -> bool:
        for i in range(len(s)+1):
            b=s[i:]+s[:i]
        
            if b==g:
                break
            
        return b==g
            
        
