class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        c=1
        b=0
        for i in nums:
            if i!=0:
                c=c*i
            if i==0:
                b=b+1
        if b>0:
            for i in nums:
                if i==0 and b==1:
                    l.append(c)
                else:
                    l.append(0)
        else:
            for i in nums:
                b=c//i
                l.append(b)
        
        return l


        
