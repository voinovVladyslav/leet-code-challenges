# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = self.dfs([root])
        return depth

    def dfs(self, nodes: list[TreeNode], depth=0):
        if not nodes:
            return depth
        if not nodes[0]:
            return depth
        next_level = []
        print('depth:', depth, 'nodes:', nodes)
        for node in nodes:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        return self.dfs(next_level, depth+1)


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
print(s.maxDepth(tree))
