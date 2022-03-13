# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        new_head = ListNode(0, head)
        cur = new_head

        while cur.next and cur.next.next:
            tmp1 = cur.next
            tmp2 = tmp1.next
            tmp3 = tmp2.next

            cur.next = tmp2
            tmp2.next = tmp1
            tmp1.next = tmp3

            cur = tmp1
        return new_head.next
