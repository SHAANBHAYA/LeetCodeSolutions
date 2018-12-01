# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:

    first_node=None
    last_node=None
    prev_node=None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.findConflictingNodes(root)
        temp_val=self.last_node.val
        self.last_node.val=self.first_node.val
        self.first_node.val=temp_val


    def findConflictingNodes(self,root):

        if root==None:
            return

        self.findConflictingNodes(root.left)
        if self.prev_node==None:
            self.prev_node=root
        else:
            if self.first_node is None :
                if self.prev_node.val>root.val:
                    self.first_node=self.prev_node
                    self.last_node=root
            else:
                if self.prev_node.val>root.val:
                    self.last_node=root
            self.prev_node=root

        self.findConflictingNodes(root.right)




root=TreeNode(3)
root_left=TreeNode(1)
root_right=TreeNode(4)
root.left=root_left
root.right=root_right
root_left.left=None
root_left.right=None
root_right.left=TreeNode(2)


a=Solution()
a.recoverTree(root)