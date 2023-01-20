# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list2:
            return list1
        if not list1:
            return list2

        if list1.val > list2.val:
            merged_head = list2
            current1 = list1
            current2 = list2.next
        else:
            merged_head = list1
            current1 = list1.next
            current2 = list2
        tail = merged_head

        while current1 or current2:

            if not current1:
                tail.next = current2
                break
            if not current2:
                tail.next = current1
                break

            if current1.val > current2.val:
                tail.next = current2
                tail = current2
                current2 = current2.next
            else:
                tail.next = current1
                tail = current1
                current1 = current1.next

        return merged_head


list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))

s = Solution()
res = s.mergeTwoLists(list1, list2)

node = res
while node:
    print(node.val)
    node = node.next
