class Solution:
    def transformArray(self, n: List[int]) -> List[int]:
        l=[]
        for i in n:
            l.append(i%2)
        l.sort()
        return l
