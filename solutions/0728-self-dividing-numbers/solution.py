class Solution:
    def selfDividingNumbers(self, l: int, r: int) -> List[int]:
        k=[]
        for i in range(l,r+1):
            t=i
            u=True
            while(i!=0):
                b=i%10
                i=i//10
                if b==0 or t%b!=0:
                    u=False
                    break
            if u:
                k.append(t)
                
            
        return k

            
        
