class Solution:
    def calPoints(self, o: List[str]) -> int:
        l=[]
        for i in o:
            if i=="C":
                l.pop()
            elif i=="D":
                b=l[len(l)-1]
                k=2*b
                l.append(k)
            elif i=="+":
                l.append(l[-1]+l[-2])
            else:
                l.append(int(i))

            
        return sum(l)

                
            
    
        
