class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        b=nums[::-1]
        return nums+b   
