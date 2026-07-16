class Solution:
    def isArraySpecial(self, n: List[int]) -> bool:
        if len(n)<=1:
            return True
        for i in range(len(n)-1):
            if n[i]%2==n[i+1]%2:
                return False
        return True





        
