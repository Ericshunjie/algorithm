# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        newhead = head.next
        # head.next = self.swapPairs(newhead.next)
        newhead.next = head
        newhead.next.next = self.swapPairs(head.next.next)
        return newhead

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
s = Solution()
r = s.swapPairs(head)