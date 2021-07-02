#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA or headB) is None:
            return None

        sizeA = 0
        sizeB = 0

        runnerA = headA
        runnerB = headB

        while runnerA:
            sizeA += 1
            runnerA = runnerA.next

        while runnerB:
            sizeB += 1
            runnerB = runnerB.next

        runnerA = headA
        runnerB = headB

        if sizeA > sizeB:
            for i in range(sizeA - sizeB):
                runnerA = runnerA.next
        elif sizeB > sizeA:
            for i in range(sizeB - sizeA):
                runnerB = runnerB.next

        while (runnerB or runnerA):
            if runnerA == runnerB:
                return runnerA
            runnerA = runnerA.next
            runnerB = runnerB.next

        return None
# @lc code=end
