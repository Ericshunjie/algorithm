# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        # 转置链表
        def reverse_l(node):
            pre = None
            while node:
                next_node = node.next
                node.next = pre
                pre = node
                node = next_node
            return pre

        l1rever = reverse_l(l1)
        l2rever = reverse_l(l2)

        # 相加
        pre = None
        add_flag = 0
        while l1rever or l2rever:
            val1 = l1rever.val if l1rever else 0
            val2 = l2rever.val if l2rever else 0
            val = val1 + val2
            val += add_flag
            add_flag = 1 if val > 9 else 0
            val = val if val <= 9 else val - 10
            node = ListNode(val)
            if pre:
                pre.next = node
            pre = node
            l1rever = l1rever.next if l1rever else None
            l2rever = l1rever.next if l2rever else None
        if add_flag:
            pre.next = ListNode(1)
            pre = pre.next
        return reverse_l(pre)









