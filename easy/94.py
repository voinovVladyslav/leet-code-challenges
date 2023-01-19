class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [
                root.val
            ] + self.inorderTraversal(root.right)


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

s = Solution()
print(s.inorderTraversal(tree))
