"""正则匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
 
示例 1：
输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:
输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：
输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4：
输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5：
输入：s = "mississippi" p = "mis*is*p*."
输出：false
"""
"""
思路:动态规划
状态: s[i..j]的匹配结果为dp(i,j)
选择: 
1. 成功匹配
    1.1 s[i]==p[j]||p[j]=='.'
        1.1.1 p[j+1]=='*' // *号时匹配若干次
2. 失败匹配
    2.1 s[i]!=p[j]
     2.1.1 p[j+1]=='*' // 由于可以匹配0次，避免失败了失败匹配
    
base case: function dp
/
"""


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def dp(i, j) -> bool:
            # j先走完
            if j == n:
                return i == m
            # i 先走完，检测p[j..]是否为a*b*c*类型
            if i == m:
                if (n - j) % 2:
                    return False
                for k in range(j, n, 2):
                    if k + 1 < n and p[k + 1] != '*':
                        return False
                return True
            if s[i] == p[j] or p[j] == '.':
                if j < n - 1 and p[j + 1] == '*':
                    # 若干匹配
                    return dp(i, j + 2) or dp(i + 1, j)
                else:
                    # 常规匹配
                    return dp(i + 1, j + 1)
            else:
                if j < n - 1 and p[j + 1] == '*':
                    # 0次匹配
                    return dp(i, j + 2)
                else:
                    return False

        return dp(0, 0)

    # FIXME: 使用备忘录memo
    def isMatch2(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = dict()


        def dp(i, j) -> bool:
            # j先走完
            if j == n:
                return i == m
            # i 先走完，检测p[j..]是否为a*b*c*类型
            if i == m:
                if (n - j) % 2:
                    return False
                for k in range(j, n, 2):
                    if k + 1 < n and p[k + 1] != '*':
                        return False
                return True
            key = str(i) + "," + str(j)
            if key in memo:
                return memo[key]
            res = False
            if s[i] == p[j] or p[j] == '.':
                if j < n - 1 and p[j + 1] == '*':
                    # 若干匹配
                    res = dp(i, j + 2) or dp(i + 1, j)
                else:
                    # 常规匹配
                    res = dp(i + 1, j + 1)
            else:
                if j < n - 1 and p[j + 1] == '*':
                    # 0次匹配
                    res = dp(i, j + 2)
                else:
                    res = False

            memo[key] = res
            return res
        return dp(0, 0)


solution = Solution()
p = solution.isMatch2("aa", "a*")
print(p)
