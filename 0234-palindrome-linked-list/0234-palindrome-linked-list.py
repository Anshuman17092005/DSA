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
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast =fast.next.next
        temp = slow.next
        slow.next = None
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True