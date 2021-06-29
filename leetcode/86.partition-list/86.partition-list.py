# @before-stub-for-debug-begin
from python3problem86 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        beforePointer = beforeHead = ListNode(0)
        afterPointer = afterHead = ListNode(0)

        while head:
            if head.val < x:
                beforePointer.next = head
                beforePointer = beforePointer.next
            else:
                afterPointer.next = head
                afterPointer = afterPointer.next

            head = head.next

        afterPointer.next = None

        beforePointer.next = afterHead.next

        return beforeHead.next

        # dummyHead = ListNode(0)
        # dummyHead.next = head
        # runner = dummyHead
        # secondListRunner = ListNode(0)
        # secondListHead = secondListRunner

        # while runner.next:
        #     if runner.next.val >= x:
        #         secondListRunner.next = ListNode(runner.next.val)
        #         secondListRunner = secondListRunner.next
        #         runner.next = runner.next.next
        #         continue

        #     runner = runner.next

        # runner.next = secondListHead.next

        # return dummyHead.next

# @lc code=end
