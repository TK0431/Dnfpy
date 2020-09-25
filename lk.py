# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.max_deep = 1
        def get_next(node, deep = 2):
            if not node: return
            self.max_deep = deep if deep > self.max_deep else self.max_deep
            get_next(node.left, deep + 1)
            get_next(node.right, deep + 1)

        get_next(root.left)
        get_next(root.right)
        return self.max_deep

#[3,9,20,null,null,15,7]
n1 = None
# n2 = TreeNode(9)
# n3 = TreeNode(20)
# n4 = None
# n5 = None
# n6 = TreeNode(15)
# n7 = TreeNode(7)
# n1.left = n2
# n1.right = n3
# n3.left = n6
# n3.right = n7
s = Solution()
print(s.maxDepth(n1))
