class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[]
        s="Fizz"
        o="Buzz"
        p="FizzBuzz"
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                l.append(s)
            elif i%5==0 and i%3!=0:
                l.append(o)
            elif i%5==0 and i%3==0:
                l.append(p)
            else:
                l.append(str(i))
            
        return l
        
