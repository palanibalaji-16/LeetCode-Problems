class Solution:
    def findMaxConsecutiveOnes(self, n: List[int]) -> int:
        p=0
        l=[]
        for i in n:
            if i==1:
                p=p+1
            else:
                l.append(p)
                p=0
            
        l.append(p)

        return max(l) 
        
