class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        p=[]
        for i in nums:
            if nums.count(i)==1:
                p.append(i)
            
        return sum(p)
