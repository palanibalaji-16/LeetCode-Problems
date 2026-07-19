class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=[]
        m=set(nums)
        for i in range(1,len(nums)+1):
            if i not in m:
                n.append(i)
            
        return n
        
