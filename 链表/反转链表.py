# 题意：反转一个单链表。
#
# 示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL

#思路


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if not head:return None
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
