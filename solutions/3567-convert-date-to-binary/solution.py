class Solution:
    def convertDateToBinary(self, date: str) -> str:
        b=date.split("-")
        for i in range(len(b)):
                b[i]=bin(int(b[i]))[2:]

        return "-".join(b)
        
