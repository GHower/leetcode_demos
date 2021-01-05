from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = list()
        start, end = 0, 0
        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1]:
                end += 1
            else:
                if end - start > 1:
                    res.append([start, end])
                start = idx + 1
                end = idx + 1
        if end - start > 1:
            res.append([start, end])
        return res

    def largeGroupPositions2(self, s: str) -> List[List[int]]:
        res = list()
        count = 1
        for idx in range(len(s)):
            if idx == len(s)-1 or s[idx] != s[idx + 1]:
                if count > 2:
                    res.append([idx + 1 - count, idx])
                count = 1
            else:
                count += 1
        return res


sl = Solution()
print(sl.largeGroupPositions2("abbxxxxzyy"))
print(sl.largeGroupPositions2("aaa"))
print(sl.largeGroupPositions2("abcdddeeeeaabbbcd"))
