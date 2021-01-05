from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# TODO: createData


# FIXME: 压缩空间,temp可省略，使用j变量标记
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not  root: return []
        curr = [root]
        res = []
        while curr:
            length = len(curr)
            temp = []
            for i in range(length):
                tn = curr.pop(0)
                temp.append(tn.val)
                if tn.left:
                    curr.append(tn.left)
                if tn.right:
                    curr.append(tn.right)
            res.append(temp)
        return [res[i][::-1] if i % 2 else res[i][:] for i in range(len(res))]


# sl = Solution()
# sl.zigzagLevelOrder(TreeNode(1))

s = [1, 2, 3, 4]
print(s[::-1])
