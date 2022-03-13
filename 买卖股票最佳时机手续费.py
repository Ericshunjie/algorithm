class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        if not len(prices):
            return 0
        min_price = prices[0]
        max_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                max_price = prices[i]
            else:
                max_price = max(max_price, prices[i])

            if i == len(prices) - 1 and max_price - min_price - fee > 0:
                profit += max_price - min_price - fee
            elif (i < len(prices) - 1 and prices[i] >= prices[i + 1] + fee) and max_price - min_price - fee > 0:
                # print(max_price, min_price)
                profit += max_price - min_price - fee
                min_price = prices[i + 1]
                max_price = prices[i + 1]
        return profit

s = Solution()
r = s.maxProfit([2,2,1,1,5,5,3,1,5,4], 2)
print(r)