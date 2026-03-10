class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        res = int(str(abs(x))[::-1])  # This must line up with 'sign'
        res *= sign
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res

