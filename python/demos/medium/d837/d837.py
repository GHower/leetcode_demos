class Solution:
    # 在LeetCode中会超时
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K < 1: return 1.0

        dp = [1.0 if _ <= min(N, K + W - 1) + 1 else 0 for _ in range(K + W)]

        for i in range(K - 1, -1, -1):
            dp[i] = (sum(dp[i + 1:i + W + 1])) / W

        return dp[0]

    # 压缩状态
    def new21Game2(self, N: int, K: int, W: int) -> float:
        # if K < 1: return 1.0
        if N - K + 1 >= W: return 1.0

        dp = [1.0 if _ <= N else 0 for _ in range(K + W)]
        print(dp)
        dp[K - 1] = (N - K + 1) / W
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        print(dp)
        return dp[0]


sl = Solution()
# print(sl.new21Game(21, 17, 10))
# print(sl.new21Game(21, 17, 10))
# print(sl.new21Game(21, 17, 10))
print(sl.new21Game2(21, 17, 10))
