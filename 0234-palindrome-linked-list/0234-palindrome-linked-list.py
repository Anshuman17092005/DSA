# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        temp = slow
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        curr1 = head
        curr2 = prev
        while curr2 is not None:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return True