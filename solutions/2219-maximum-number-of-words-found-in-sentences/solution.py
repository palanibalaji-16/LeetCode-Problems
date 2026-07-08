class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        ma=0
        print(len(s))
        for i in s:
            ma=max(ma,len(i.split()))
        
        return ma

