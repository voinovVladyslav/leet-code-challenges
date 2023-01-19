# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    rev = None

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev


head = ListNode(
    val=1, next=ListNode(
        val=2, next=ListNode(
            val=3, next=ListNode(
                val=4, next=ListNode(
                    val=5, next=None)))))

s = Solution()
res = s.reverseList(head)

print('========')
node = res
while node:
    print(node.val)
    node = node.next
