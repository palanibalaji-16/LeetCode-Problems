class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l=[int(i) for i in date.split("-")]
        b=[]
        for i in l:
            o=bin(i)[2:]
            b.append(o)
        
        return "-".join(b)


        
