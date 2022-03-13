


# 题意：删除链表中等于给定值 val 的所有节点。
# Definition for singly-linked list.\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        new_head = ListNode(0, head)
        pre = new_head
        node = head
        while node:
            print(node.val, pre.val)
            if node.val == val:
                # 移除当前
                pre.next = node.next
                node.next = None
                node = pre.next
            else:
                pre = node
                node = node.next
        return new_head.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)
s = Solution()
s.removeElements(head, 6)