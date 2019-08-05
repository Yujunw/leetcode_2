'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''


class Solution:
    # 超时
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            temp = max(prices[i + 1:]) - prices[i]
            if temp > profit:
                profit = temp
        return profit

    def maxProfit_2(self, prices):
        '''
        动态规划：前i天的最大收益 = max(前i-1天的最大收益，第i天的价格减去前i-1天的价格最小值)
        :param prices:
        :return:
        '''
        if not prices:
            return 0
        # 不该去维护一个profit数组
        profit = [0] * (len(prices))
        for i in range(1, len(prices)):
            temp = prices[i] - min(prices[:i])
            profit[i] = max(profit[i - 1], temp)
        return profit[-1]

    def maxProfit_3(self, prices):
        '''
        动态规划：前i天的最大收益 = max(前i-1天的最大收益，第i天的价格减去前i-1天的价格最小值)
        :param prices:
        :return:
        '''
        if not prices:
            return 0
        # 不该去维护一个profit数组
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit_3(prices))
