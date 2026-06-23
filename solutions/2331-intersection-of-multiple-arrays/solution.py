class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l=set(nums[0])
        for i in range(len(nums)):
            l.intersection_update(nums[i])
        
        return sorted(list(l))
