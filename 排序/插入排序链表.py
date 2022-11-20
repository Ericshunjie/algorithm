class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 遍历 当后面小于前面的时候 从新开始找适合的位置
        if not head: return None
        result_head = ListNode(0)
        result_head.next = head
        node = head.next
        last = head
        while node:
            if node.val >= last.val:
                # 继续遍历
                last = node
            else:
                # 重新开始找node的位置
                # new_node.val > node.val 就是node的位置前面一个
                pre = result_head
                while pre.next.val <= node.val:
                    pre = pre.next
                # pre的next 就是node的新位置
                # 位置交换
                last.next = node.next
                node.next = pre.next
                pre.next = node
            node = last.next
        return result_head.next

s = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
r = s.insertionSortList(head)
# while r:
#     print(r.val)
#     r = r.next
