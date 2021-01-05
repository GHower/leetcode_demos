from typing import List

"""
每次选最大两石头

"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n, res = len(stones), 0

        if n == 1: return stones[0]
        if n == 2: return abs(stones[0] - stones[1])

        sorted(stones)


        return res


sl = Solution()
print(sl.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
