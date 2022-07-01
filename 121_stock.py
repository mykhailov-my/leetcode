"""
Status -> Solved by myself

Time complexity -> O(n)
Space complexity -> O(1)

Solution
1. init 3 variables -> buy, sell, profit
2. if there is higher then sell price -> move sell price
3. if there is lower price -> check what profit more previous sell or current. Any way keep sell and buy vars moving
4. check one list time what make more money
5. return profit variable
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = 0
        profit = 0
        for i in prices:
            if i > sell:
                sell = i
            if i < buy:
                profit = max(profit, sell - buy)
                buy = i
                sell = i
        profit = max(profit, sell - buy)
        return profit



if __name__ == '__main__':
    n = [7,1,5,3,6,4] # 5
    # n = [3, 2, 3, 5, 0, 1, 4]
    # n = [3, 2, 3, 5, 0, 2]
    sol = Solution()
    res = sol.maxProfit(n)
    print(f'Result --> {res}')