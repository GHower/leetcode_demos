class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        r = list()
        res = list()

        def dp(root: TreeNode, sum: int):
            # base case
            if not root: return
            r.append(root.val)
            # 没有左右子树，即叶子节点
            if not root.left and not root.right and not sum - root.val:
                res.append(r[:])
            dp(root.left, sum - root.val)
            dp(root.right, sum - root.val)
            r.pop()

        dp(root, sum)
        return res