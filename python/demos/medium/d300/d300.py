from typing import List

"""最长递增子序列

状态:以nums[i]为结尾的最长递增序列为dp[i]
选择:
base case:

"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = []
        for i in range(length):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


sl = Solution()
n = sl.lengthOfLIS([1,3,6,7,9,4,10,5,6])
print(n)
#
