class Solution:
    def firstUniqChar(self, s: str) -> int:
        b=list(s)
        l=Counter(b)
        p=""
        t=False
        for k,v in l.items():
            if v==1:
                p=k
                t=True
                break

            
        if(t):
            return s.index(p)
        else:
            return -1
            
            
      
        
