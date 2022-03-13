class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        ## 快慢指针 找到相遇节点
        ## 初始状态应该是slow = fast = head
        if not (head.next and head.next.next):
            return None
        fast = head.next.next
        slow = head.next
        while fast != slow:
            print(fast.val, slow.val)
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return None
            slow = slow.next
        # 找到相遇节点后，从head开始一个新起点，继续next直到相遇
        new = head
        while new != slow:
            print(new.val, slow.val)
            new = new.next
            slow = slow.next
        return new

head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1
s = Solution()
s.detectCycle(head)