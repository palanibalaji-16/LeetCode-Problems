class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        v=Counter(nums)
        c=False
        for k,v in v.items():
            if v==1 and k%2==0:
                b=k
                c=True
                break
            
        if(c):
            return b
        else:
            return -1
       
        
