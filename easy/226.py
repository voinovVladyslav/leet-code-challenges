class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root

    def invert(self, node: TreeNode):
        if not node:
            return

        node.left, node.right = node.right, node.left

        self.invertTree(node.left)
        self.invertTree(node.right)


tree = TreeNode(
    val=3,
    left=TreeNode(
        val=9,
        left=None,
        right=None
    ),
    right=TreeNode(
        val=20,
        left=TreeNode(
            val=15,
            left=None,
            right=None),
        right=TreeNode(
            val=7,
            left=None,
            right=None)))
