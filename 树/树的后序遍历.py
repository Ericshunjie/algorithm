 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        result = []
        stack = [root,]
        while stack:
            root = stack.pop()
            result.insert(0,root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return result
        



## 后续遍历和前序中序遍历不同，因为后续遍历需要左右两个孩子都push进去再push自己
# 转变思路，后续遍历的反序就是根 -> 右 -> 左， 可以通过广度优先构建堆栈，再逆序
# 