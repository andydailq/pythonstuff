class Solution:
    # RC O(n)
    # SC O(1)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf')
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > profit:
                profit = prices[i] - minprice
        return profit