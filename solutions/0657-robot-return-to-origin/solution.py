class Solution:
    def judgeCircle(self, m: str) -> bool:
        p=len(m)
        x,y=0,0
        for i in range(p):
            if m[i]=="U":
                y=y+1
            elif m[i]=="D":
                y=y-1
            elif m[i]=="R":
                x=x+1
            elif m[i]=="L":
                x=x-1
            

        return x==y==0
            
            
