from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = 0
        for num in nums:
            t = t ^ num
        return t


sl = Solution()
n = sl.singleNumber([1, 2, 2, 4, 5, 5, 6, 6, 4])
print(n)