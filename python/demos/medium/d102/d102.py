from queue import Queue
from typing import List

# 树的层序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# TODO: createData


# FIXME: 压缩空间,temp可省略，使用j变量标记
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        qe = Queue()
        if root:
            qe.put(root)
        res = []
        while not qe.empty():
            lenght = qe.qsize()
            temp = []
            for i in range(lenght):
                tn = qe.get()
                temp.append(tn.val)
                if tn.left:
                    qe.put(tn.left)
                if tn.right:
                    qe.put(tn.right)
            res.append(temp)
        return res


sl = Solution()
sl.levelOrder(TreeNode(1))
