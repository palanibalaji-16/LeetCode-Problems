class Solution:
    def triangleType(self, n: List[int]) -> str:
        n.sort()
        if n[0]+n[1]<=n[2]:
            return "none"
        if n[0]==n[1]==n[2]:
            return "equilateral"
        if n[0]==n[1] or n[1]==n[2]:
            return "isosceles"
        
        
        return "scalene"

