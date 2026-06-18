class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            s=str(i)
            for i in range(len(s)):
                l.append(int(s[i]))
            
        
        return l
        
