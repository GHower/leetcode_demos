from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once


sl = Solution()
n = sl.singleNumber([1, 2, 2, 2, 5, 5, 5, 6, 6, 6])
print(n)
