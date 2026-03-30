from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s=-1
        l=Counter(arr)
        for k,v in l.items():
            if(k==v):
                if(k>s):
                    s=k
            
        return s


        
