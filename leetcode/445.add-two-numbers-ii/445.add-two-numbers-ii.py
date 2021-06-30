#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        n1 = n2 = 0

        while l1:
            n1 = n1*10 + l1.val
            l1 = l1.next

        while l2:
            n2 = n2*10 + l2.val
            l2 = l2.next

        l3 = l3Head = ListNode(0)

        for d in str(n1 + n2):
            l3.next = ListNode(int(d))
            l3 = l3.next

        return l3Head.next
# @lc code=end
