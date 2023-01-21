# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        return self.level_traversal([root], [])

    def level_traversal(self, nodes: list[TreeNode], levels):
        if not nodes:
            return levels
        next_level = []
        current_level_vals = []
        while nodes:
            node = nodes.pop(0)
            current_level_vals.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        levels.append(current_level_vals)
        return self.level_traversal(next_level, levels)


tree = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(
            val=3,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=4,
            left=None,
            right=None
        )
    ),
    right=TreeNode(
        val=2,
        left=TreeNode(
            val=4,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=3,
            left=None,
            right=None
        )
    )
)

s = Solution()
print(s.levelOrder(tree))
