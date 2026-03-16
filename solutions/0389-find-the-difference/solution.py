from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Subtracting counts leaves only the extra character
        diff = Counter(t) - Counter(s)
        return list(diff.keys())[0]

