class Solution:
    def addDigits(self, num: int) -> int:

        while(num>=10):
            num=int(num/10)+num%10
        return int(num)

        
