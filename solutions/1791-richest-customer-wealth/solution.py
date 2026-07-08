class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        l=[]
        for i in a:
            l.append(sum(i))
        return max(l)

        
