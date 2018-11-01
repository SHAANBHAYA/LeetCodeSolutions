# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        index=1
        if head is None:
            return head
        old_pointer_even=new_pointer_even=head
        new_pointer_even=head.next

        head_of_odd=ListNode(10)
        new_pointer_odd=head_of_odd
        while new_pointer_even is not None:
            if index%2!=0:
                old_pointer_even.next=new_pointer_even.next
                new_pointer_even.next=None
                new_pointer_odd.next=new_pointer_even
                new_pointer_odd=new_pointer_odd.next
                new_pointer_even=old_pointer_even.next
            else:
                new_pointer_even=new_pointer_even.next
                old_pointer_even=old_pointer_even.next
            index+=1
        old_pointer_even.next=head_of_odd.next
        return head




sol=Solution()
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
sol.oddEvenList(head)