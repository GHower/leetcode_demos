"""
以s[i]为结尾的回文子序列数为dp[i]
"""


class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:

        dp = [1]
        n = len(S)

        for i in range(1, n):
            dp.append(1)
            for j in range(i+1):
                if S[i] == S[j]:
                    dp[i] = sum(dp[0:i-1])+1
                else:
                    dp[i] = dp[i-1]+1
        # for i in range(n):
        print(dp)
        return 0


sl = Solution()
sl.countPalindromicSubsequences('bccb')
