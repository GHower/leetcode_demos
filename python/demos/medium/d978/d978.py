from typing import List

"""最长湍流子数组
动态规划
状态: 
2. 以A[i]为结尾的最大上升湍流为dp[i][0],下降为dp[i][1]
注: 这里上升湍流是指最后一段为符合上升条件,即k为奇数时A[k]>A[k+1]
选择:
1. A[i]符合上升湍流
    dp[i][0] = dp[i][1]+1 , if A[k]>A[k+1]
2. A[i]符合下降湍流
    dp[i][1] = dp[i-1][0] +1, if A[k]<A[k+1]
    
base case:
    dp[i][0]=dp[i][1]=1
"""


class Solution:
    # FIXME: 空间优化，可省略dp数组
    # 每次只用到上一次的值，即状态是相邻的，可以压缩
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2: return n
        # base case
        #dp = [[1] * 2 for i in range(n)]
        res = 0
        up = 0
        down = 0
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                #dp[i + 1][0] = dp[i][1] + 1
                up1 = down+1
            else:
                up1 = 1
            if arr[i] < arr[i + 1]:
                #dp[i + 1][1] = dp[i][0] + 1
                down1 = up + 1
            else:
                down1 = 1
            up = up1
            down = down1
            res = max(res, up,down)
        # for i in dp:
        #     print(i)
        return res

sl = Solution()
result = sl.maxTurbulenceSize([0,8,45,88,48,68,28,55,17,24])
print(result)
