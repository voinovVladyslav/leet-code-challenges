# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __eq__(self, obj) -> bool:
        return self.val == obj.val and self.next == self.next


class Solution:
    def getIntersectionNode(self, headA=ListNode, headB=ListNode) -> ListNode:
        tailA = headA
        tailB = headB
        lenA = 0
        lenB = 0
        while tailA.next or tailB.next:
            if tailA.next:
                tailA = tailA.next
                lenA += 1
            if tailB.next:
                tailB = tailB.next
                lenB += 1

        if tailA != tailB:
            return None

        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        else:
            for _ in range(lenB - lenA):
                headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA


headA = ListNode(
    val=4,
    next=ListNode(
        val=1,
        next=ListNode(
            val=8,
            next=ListNode(
                val=4,
                next=ListNode(
                    val=5,
                    next=None
                )
            )
        )
    )
)
headB = ListNode(
    val=5,
    next=ListNode(
        val=6,
        next=ListNode(
            val=1,
            next=ListNode(
                val=8,
                next=ListNode(
                    val=4,
                    next=ListNode(
                        val=5,
                        next=None
                    )
                )
            )
        )
    )
)

s = Solution()
print(s.getIntersectionNode(headA, headB))
