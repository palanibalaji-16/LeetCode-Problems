class Solution:
    def heightChecker(self, h: List[int]) -> int:
        l=sorted(h)
        c=0
        for i in range(len(h)):
            if h[i]!=l[i]:
                c=c+1
        return c 
