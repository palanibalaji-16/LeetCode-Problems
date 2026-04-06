class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        l=[]
        s=Counter(str(n))
        minx=min(s.values())
        for k,v in s.items():
            if(v==minx):
                l.append(int(k))     
        return min(l)
    
