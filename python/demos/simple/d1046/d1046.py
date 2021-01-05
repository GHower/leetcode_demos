from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heaps = [-stone for stone in stones]
        heapq.heapify(heaps)
        # print([heapq.heappop(heaps) for _ in range(len(heaps))])
        while len(heaps) > 1:
            s1, s2 = heapq.heappop(heaps), heapq.heappop(heaps)
            if s1 != s2:
                heapq.heappush(heaps, s1 - s2)
        if heaps: return heaps[0]
        return 0


sl = Solution()
result = sl.lastStoneWeight([10, 20, 30, 40, 2, 8, 6, 4, 3, 3, 3, 1, 7, 5, 60])
print(result)
