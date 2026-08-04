class Solution:
    def findMissingElements(self, n: List[int]) -> List[int]:
        n.sort()
        p=[]
        j=0
        for i in range(n[0],n[-1]):
            if n[j]!=i:
                p.append(i)
            else:
                j=j+1
        return p
      
    
        
