class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        maxp = 0


        while r < len(prices):

            if prices[l] > prices[r]:
                l = r
            
            maxp = max(prices[r] - prices[l], maxp)
            r += 1

        return maxp










        