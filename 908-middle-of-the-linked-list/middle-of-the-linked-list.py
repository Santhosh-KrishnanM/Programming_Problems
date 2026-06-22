# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def display(self, slow):
        current = slow
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        self.display(slow)
        print(slow)
        return slow