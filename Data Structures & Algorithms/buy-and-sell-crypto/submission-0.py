class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxp = 0


        for price in range(len(prices)):
            currentmax = 0
            r = price + 1

            while r < len(prices):
                currentmax = max(prices[r] - prices[price], currentmax)
                r+=1
            maxp = max(currentmax, maxp)

        return maxp










        