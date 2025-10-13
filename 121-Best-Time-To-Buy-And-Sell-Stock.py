class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxp = 0

        while r < len(prices):
            p = prices[r] - prices[l]
            maxp = max(p, maxp)
            if prices[l] > prices[r]:
                l = r
            else:
                r +=1
        return maxp

            
