class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False

        b=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                b=b+i
                if i*i!=num:
                    b=b+num//i

        return num==b

            
        return b==num

        
