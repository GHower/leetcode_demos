from typing import List

"""K站中转最便宜的航班
######动态规划
状态: 
1. 以src为起点，中转k站后的最便宜价格为dp[end][k]
选择: 
base case: 
    将dp数组初始化类似矩阵
    将中转0站的价格载入dp[src][0]
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # base case:
        dp = [[1 << 31 for i in range(K + 1)] for i in range(n)]
        dp[src][0] = 0
        for flight in flights:
            start = flight[0]
            end = flight[1]
            prince = flight[2]
            if start == src:
                dp[end][0] = min(dp[end][0], prince)
        # print(dp)
        for k in range(1,K+1):
            for flight in flights:
                print(dp)
                start = flight[0]
                end = flight[1]
                prince = flight[2]
                dp[end][k] = min(dp[end][k - 1],
                                 dp[end][k],
                                 dp[start][k - 1] + prince)
        print(dp)

        return -1 if dp[dst][K] == 1 << 31 else dp[dst][K]


sl = Solution()
res = sl.findCheapestPrice(n=3,
                           flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                           src=0, dst=2, K=1)
print(res)
