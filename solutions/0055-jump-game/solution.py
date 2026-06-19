class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g=0
        for i in nums:
            if g<0:
                return False
            elif i > g:
                g=i
            g=g-1
        return True

        
