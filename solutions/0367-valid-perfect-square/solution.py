class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        d=num**0.5
        if(d.is_integer()):
            return True
        else:
            return False

