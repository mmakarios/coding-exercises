#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head

        reversedHead = None
        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = reversedHead
            reversedHead = slow
            slow = temp

        if fast:
            slow = slow.next

        while reversedHead and reversedHead.val == slow.val:
            slow = slow.next
            reversedHead = reversedHead.next

        return not reversedHead

# @lc code=end
