class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        j=nums[-1]
        c=nums[-1]

        for i in range(1,k):
            j=j+1
            c=c+j

        
        return c

        
