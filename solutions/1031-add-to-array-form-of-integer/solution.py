import sys


sys.set_int_max_str_digits(20000)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        b = "".join(map(str, num))
        c = int(b) + k
        return [int(x) for x in str(c)]

