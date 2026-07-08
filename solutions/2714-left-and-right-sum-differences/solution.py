class Solution:
    def leftRightDifference(self, n: List[int]) -> List[int]:
        l=[0]
        k=[0]
        r=[]
        for i in range(len(n)-1):
            l.append(l[i]+n[i])
        for j in range(len(n)-1,-1,-1):
            k.append(k[-1]+n[j])
        k.pop()
        k.reverse()
        for i in range(len(n)):
            r.append(abs(l[i]-k[i]))
        
        return r

        
            

        
