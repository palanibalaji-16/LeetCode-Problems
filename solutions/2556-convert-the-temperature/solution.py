class Solution:
    def convertTemperature(self, c: float) -> List[float]:
        l=[]
        k=c+273.15
        f=c*1.80+32.00
        l.append(k)
        l.append(f)
        return l

        
