class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        result = head
        # h = result
        node = head.next
        result.next = None
        while node:
            print(result.val)
            nextnode = node.next
            r = result
            pre = result
            while r and node.val > r.val:
                r = r.next
                pre = r
            if r:
                # r.pre = node
                if r == result:
                    node.next = result
                    result = node
                else:
                    pre.next = node
                    node.next = r
            else:
                pre.next = node
            node = nextnode
        return result

s = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
r = s.insertionSortList(head)
# while r:
#     print(r.val)
#     r = r.next
