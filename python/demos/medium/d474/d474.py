from typing import List

"""474. 一和零
状态
1. i个0,j个1时的最大子集为dp[i][j],则dp[m][n]为所求答案
选择：
1-当前字符串在最大集合中，zeros,ones为当前字符串的0和1个数
    1+dp[i-zeros][j-ones]
2-当前字符串不在最大集合中
    dp[i][j]
遍历顺序: 自下而上，自左而右
"""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        if not length: return 0
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for s in strs:
            z, o = self.zeroAndOne(s)
            for i in range(m, z - 1, -1):
                for j in range(n, o - 1, -1):
                    dp[i][j] = max(1+dp[i - z][j - o], dp[i][j])
        for i in range(m + 1):
            print(dp[i])
        return dp[m][n]

    def zeroAndOne(self, str) -> (int, int):
        zero, one = 0, 0
        for i in str:
            if i == "0":
                zero += 1
            else:
                one += 1
        return zero, one


sl = Solution()
res = sl.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
print(res)
