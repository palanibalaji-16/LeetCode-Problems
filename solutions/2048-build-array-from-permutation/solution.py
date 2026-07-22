class Solution:
    def buildArray(self, n: List[int]) -> List[int]:
        l=[]
        for i in range(len(n)):
            l.append(n[n[i]])
        return l
        
