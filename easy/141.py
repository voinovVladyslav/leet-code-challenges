# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        visited = []
        while node:
            if node in visited:
                return True
            visited.append(node)
            node = node.next
        return False
