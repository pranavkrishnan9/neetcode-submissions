# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #input = two non empty linked lists l1, l2 where each list represents the digits of a non-negative number stored in reverse order
        #output = sum of the two non-negative numbers stored as a linked list in reverse order

        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
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
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            tail.next = ListNode(digit)
            tail = tail.next
        return dummy.next


