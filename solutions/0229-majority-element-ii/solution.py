class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        v=Counter(nums)
        l=[]
        
        for k,v in v.items():
            if v>len(nums)//3 :
                l.append(k)
                




        
        return l

        
        
