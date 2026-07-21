class Solution:
    def recoverOrder(self, o: List[int], f: List[int]) -> List[int]:
        l=[]
        for i in o:
            if i in f:
                l.append(i)
            
        return l
        
