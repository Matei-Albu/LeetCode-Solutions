# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            sum = carry
            if l1 and l2:
                sum = l2.val + l1.val + carry
            elif l1 and not l2:
                sum = l1.val + carry
            elif l2 and not l1:
                sum = l2.val + carry
            carry = 0
            if sum >= 10:
                carry += 1
                sum = sum - 10
                curr.next = ListNode(sum)
            else:
                curr.next = ListNode(sum)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next
