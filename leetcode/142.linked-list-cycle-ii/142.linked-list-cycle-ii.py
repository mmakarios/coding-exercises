#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Floyd's Tortoise and Hare Cycle Detection Algorithm
        if head == None:
            return None

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

        # Other approach without using python's while else, and using fast = head.next

        # slow = head
        # fast = head.next

        # while slow != fast:
        #     if fast == None or fast.next == None:
        #         return None

        #     slow = slow.next
        #     fast = fast.next.next

        # fast = head
        # since fast starts at head.next, we need to move slow one step forward
        # slow = slow.next

        # while slow != fast:
        #     slow = slow.next
        #     fast = fast.next

        # return slow
# @lc code=end
