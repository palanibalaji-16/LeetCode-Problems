class Solution:
    def shiftGrid(self, g: List[List[int]], k: int) -> List[List[int]]:
        r=len(g)
        co=len(g[0])
        l=[g[i][j] for i in range(len(g)) for j in range(len(g[0]))]
        k=k%len(l)
        p=l[-k:]+l[:-k]
        o=[[0]*co for i in range(r)]
        c=0
        for i in range(r):
            for j in range(co):
                o[i][j]=p[c]
                c=c+1


        return o        
