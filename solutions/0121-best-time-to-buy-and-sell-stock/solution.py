class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=prices[0]
        maprofit=0
        for i in range(1,len(prices)):
            ma=prices[i]-mi
            maprofit=max(ma,maprofit)
            mi=min(mi,prices[i])
        
        return maprofit

        
        
