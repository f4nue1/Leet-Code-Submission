# Last updated: 9/18/2026, 2:30:49 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: ListNode | None) -> ListNode | None:
8        slow, fast = head, head
9
10        while fast and fast.next:
11            slow = slow.next
12            fast = fast.next.next
13        return slow
14        
15        