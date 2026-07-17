class Solution:
    def checkIfPangram(self, s: str) -> bool:
        a="abcdefghijklmnnnopqrstuvwxyz"
        for i in a:
            if i not in s:
                return False
            
        return True
