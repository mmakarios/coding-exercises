#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        second = head

        for i in range(n):
            first = first.next

        if first == None:
            return head.next

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head
# @lc code=end
