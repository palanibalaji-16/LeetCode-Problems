
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        l=Counter(nums)
        ma=-1
        m=-1
        for k,v in l.items():
            if(k%2==0):
                if v>ma:
                    ma=v
                    m=k
                elif v==ma:
                    m=min(m,k)   
        return m
