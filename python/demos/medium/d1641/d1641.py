"""统计字典序元音字符串的数目
一、 动态规划
状态:
1. 以s[i]为开头，字符长度为j的字符串数量为dp[i][j]
    则sum(dp[n][j])为所求
选择:
base case:
    s[4]即u开头的字符串总是为1
        即 dp[4][..]=1
"""


class Solution:
    #FIXME: 仅使用相邻状态，可以压缩空间
    def countVowelStrings(self, n: int) -> int:
        dp = [[1 for j in range(5)] for i in range(n)]
        # print(dp)
        for i in range(1, n):
            for j in range(3, -1, -1):
                dp[i][j] = dp[i][j+1] + dp[i-1][j]
        for d in dp:
            print(d)
        return sum(dp[n-1])


sl = Solution()
result = sl.countVowelStrings(2)
print(result)
