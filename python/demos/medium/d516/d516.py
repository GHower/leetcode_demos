# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
# 示例 1:
# 输入: "bbbab"
# 输出:  4
# 一个可能的最长回文子序列为 "bbbb"。

# 示例 2:
# 输入: "cbbd"
# 输出: 2
# 一个可能的最长回文子序列为 "bb"。
# 提示：
# 1 <= s.length <= 1000
# s 只包含小写英文字母

# 思路：动态规划
# 状态: s[i..j]的最长回文子序列为dp[i][j]
# base case: dp[i][i]=1,只有自身一个字符，回文数必然为1，且不存在i>j
# 选择:
# 1. s[i] == s[j]
#      则s[i]和s[j]必然构成新回文，长度+2
# 2. s[i] != s[j]
#       寻找s[i]和s[j]谁构成的回文子序列更长


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            # 基础状态
            dp[i][i] = 1
        # for i in range(n):
        #     for j in range(n):
        #         print(dp[i][j]," ",end="")
        #     print("\n")
        # 自下而上，自左而右
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # for i in range(n):
        #     for j in range(n):
        #         print(dp[i][j]," ",end="")
        #     print("\n")
        return dp[0][n - 1]

    # FIXME: 使用备忘录
    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            # 基础状态
            dp[i][i] = 1
        # for i in range(n):
        #     for j in range(n):
        #         print(dp[i][j]," ",end="")
        #     print("\n")
        # 自下而上，自左而右
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # for i in range(n):
        #     for j in range(n):
        #         print(dp[i][j]," ",end="")
        #     print("\n")
        return dp[0][n - 1]

solution = Solution()
res = solution.longestPalindromeSubseq("bbbab")
print(res)
