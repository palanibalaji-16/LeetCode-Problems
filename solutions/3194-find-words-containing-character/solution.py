class Solution:
    def findWordsContaining(self, w: List[str], x: str) -> List[int]:
        l=[]
        for i in range(len(w)):
            if x in w[i]:
                l.append(i)
        
        if len(l)==0:
            return []
        else:
            return l
