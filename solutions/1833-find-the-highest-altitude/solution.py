class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        b=0
        maxx=0
        for i in gain:
            b=b+i
            maxx=max(maxx,b)
        
        return maxx
        
