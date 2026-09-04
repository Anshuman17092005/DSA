# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,head):
        prev = None
        temp = head
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return None
        prev = self.reverse(head)
        if n == 1:
            prev = prev.next
            return self.reverse(prev)
        i = 0
        curr = prev
        while i < n-2:
            i += 1
            curr = curr.next
        curr.next = curr.next.next
        return self.reverse(prev)