#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        multiplier = 1
        # l3 = ListNode(0, None)

        while l1 or l2:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            sum += (l1Val + l2Val) * multiplier
            multiplier *= 10
            # print((l1.val or 0) + (l2.val or 0))
            # print(l1.val, l2.val)

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # for i in str(sum):
        # print(list(map(int, str(sum)))[1::])
        return self.createLinkedList(list(map(int, reversed(str(sum)))))

        # return l3

    def createLinkedList(self, sum):
        if sum is None:
            return None
        return ListNode(sum[0], self.createLinkedList(sum[1::] or None))
# @lc code=end
