# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or k == 0 or not head.next:
            return head

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length +=1

        k = k % length
        if k == 0:
            return head
            
        tail.next = head

        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
    
        return new_head