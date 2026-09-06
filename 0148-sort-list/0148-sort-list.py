# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        slow = head
        fast =head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        leftHead = head
        rightHead = middle.next
        middle.next = None
        leftHead = self.sortList(leftHead)
        rightHead = self.sortList(rightHead)
        return self.merge(leftHead,rightHead)
    def merge(self,head1,head2):
        l1 = head1
        l2 = head2
        dummy = ListNode()
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                temp = l1
                l1 = l1.next
            else:
                temp.next = l2
                temp = l2
                l2 = l2.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next