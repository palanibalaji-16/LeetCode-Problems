class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n, '032b')   
        c=b[::-1]
        return int(c,2)
