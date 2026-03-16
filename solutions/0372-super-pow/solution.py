class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b=[int(i) for i in b]
        c=int("".join(map(str,b)))
        return pow(a,c,1337)
        
