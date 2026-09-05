# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        temp = dummy
        c = 0
        while l1 or l2:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            else:
                s += 0
            if l2:
                s += l2.val
                l2 = l2.next
            else:
                s += 0
            s += c
            c = s // 10
            s = s % 10
            temp.next = ListNode(s)
            temp = temp.next
        if c != 0:
            temp.next = ListNode(c)
            temp = temp.next 
        return dummy.next