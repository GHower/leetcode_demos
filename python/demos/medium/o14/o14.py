"""
绳长为n时，最大乘积为dp[n]
"""


class Solution:
    # 动规
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        dp = [0 for i in range(max(6, n + 1))]
        dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 2, 3, 4, 6
        if n < 6: return dp[n]

        for i in range(6, n + 1):
            dp[i] = max(dp[i - 3] * 3, dp[i - 2] * 2)
        return dp[n] % int(1e9 + 7)

    # 贪心
    def cuttingRope2(self, n: int) -> int:
        if n<6:
            return n-1 if n<=3 else int((n/3)*2)*2
        n_3 = int(n / 3) - 1
        n_s = n % 3
        # base 分别是剩余长度为1,2,0时的情况
        base = [3, 4, 2]
        res = pow(3, (n_3+1 if n_s==2 else n_3)) * base[n_s]
        return res % int(1e9 + 7)

    # 贪心2
    def cuttingRope3(self, n: int) -> int:
        if n <= 3: return n - 1
        nl = 0
        mul = 1
        mod = int(1e9 + 7)
        while nl < n - 4:
            mul = mul * 3
            nl += 3
            # print(mul)
        return (mul * (n - nl)) % mod
        # return mul * (n - nl)


sl = Solution()
# print(sl.cuttingRope(3))
# print(sl.cuttingRope(6))
# print(sl.cuttingRope(7))
# print(sl.cuttingRope(10))
# print(sl.cuttingRope2(4))
# print(sl.cuttingRope2(5))
print(sl.cuttingRope2(11))
# print(sl.cuttingRope2(120))
# print(sl.cuttingRope2(1000))
