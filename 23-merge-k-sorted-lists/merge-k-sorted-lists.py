# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = ListNode() 
        current = result
        for i, head in enumerate(lists):
                if head:
                    heapq.heappush(heap, (head.val, i, head))
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return result.next