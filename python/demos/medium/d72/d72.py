"""编辑距离
状态 s1[0..i] 和s2[0..j]的最小编辑距离是dp(i,j)
选择
    1. 插入
    2. 删除
    3. 替换
base case
    j<0 ： s2是空串，则s1需要删除i次
    i<0： s1是空串，则s2需要插入j次

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lm, ln = len(word1), len(word2)
        memo = dict()

        def dp(i, j) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if j < 0: return i + 1
            if i < 0: return j + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                # 分别做插入，删除，替换
                memo[(i, j)] = min(dp(i, j - 1), dp(i - 1, j), dp(i - 1, j - 1)) + 1
            return memo[(i, j)]

        return dp(lm - 1, ln - 1)

    ''' dp数组解法'''

    def minDistance2(self, word1: str, word2: str) -> int:
        lm, ln = len(word1), len(word2)
        dp = [[0 for j in range(ln+1)] for i in range(lm+1)]

        for i in range(1, lm+1):
            dp[i][0] = i
        for j in range(1, ln+1):
            dp[0][j] = j
        for i in range(1, lm+1):
            for j in range(1, ln+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[lm][ln]
        # print(dp)
        # return 0

solution = Solution()

num = solution.minDistance2("horse", "ros")
print(num)
