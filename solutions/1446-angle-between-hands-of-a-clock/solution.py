class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12:
            hour=0
        b=abs(30*hour-5.5*minutes)
        return float(min(b,360-b))

        
