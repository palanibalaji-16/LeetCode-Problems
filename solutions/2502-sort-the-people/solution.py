class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        d=dict(zip(h,n))
        b=dict(sorted(d.items(),reverse=True))
        l=[]
        for k,v in b.items():
            l.append(v)
        

        return l
        
