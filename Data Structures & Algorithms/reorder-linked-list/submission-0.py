# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0, n-1, 1, n-2, 2, n-3, 3
        # n = len(list)
        #initialize slow and fast ptrs 
        slow = head
        fast = head

        #when the end of the linked list has been found, fast.next = None and slow will be at the halfway point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        right = slow.next
        #isolate second half from first half
        slow.next = None

        prev = None
        curr = right
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        left = head
        right = prev
        while right:
            left_dummy = left.next
            right_dummy = right.next

            left.next = right
            right.next = left_dummy

            left = left_dummy
            right = right_dummy


                
