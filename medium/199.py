# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        return self.dfs(root, {}, 1).values()

    def dfs(self, node: TreeNode, see_from_right: dict, level: int):
        if not node:
            return see_from_right
        see_from_right[level] = node.val
        if node.left:
            self.dfs(node.left, see_from_right, level+1)
        if node.right:
            self.dfs(node.right, see_from_right, level+1)
        return see_from_right


tree = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=None,
        right=TreeNode(
            val=5,
            left=None,
            right=None
        )
    ),
    right=TreeNode(
        val=3,
        left=None,
        right=TreeNode(
            val=4,
            left=None,
            right=None
        )
    )
)

tree1 = TreeNode(
    val=1,
    left=None,
    right=TreeNode(
        val=3,
        left=None,
        right=None
    )
)

s = Solution()
print(s.rightSideView(tree))
