# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        slow = headA
        fast = headB
        while True:
            if slow == fast:
                return slow
            if not slow:
                slow = headB
            else:
                slow = slow.next
            if not fast:
                fast = headA
            else:
                fast = fast.next
        return None