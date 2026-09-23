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
        carry = 0
        while l1 or l2:
            total = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            total = val1+val2+carry
            carry = total // 10
            newNode = ListNode(total % 10)
            temp.next = newNode
            temp = temp.next
            
        if carry != 0:
            temp.next = ListNode(carry)
        return dummy.next