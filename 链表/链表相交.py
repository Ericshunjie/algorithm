class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        cura = headA
        curb = headB
        while cura != curb:
            # 注意条件是if cura而不是cura.next
            cura = cura.next if cura else headB
            curb = curb.next if curb else headA
        return cura