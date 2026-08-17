from typing import List

class Solution:
    def findSpecialInteger(self, items: List[int]) -> int:
        counts = {}
        b = len(items) * 0.25
        for item in items:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        for i, j in counts.items():
            if j > b:
                return i

