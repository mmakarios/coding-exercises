#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return head

        listValues = set()

        currentNode = head
        
        while currentNode is not None:
            listValues.add(currentNode.val)
            currentNode = currentNode.next

        listValues = sorted(listValues)

        currentNode = head
        currentNode.val = listValues[0]

        for value in listValues[1::]:
            currentNode = currentNode.next
            currentNode.val = value

        currentNode.next = None

        return head
# @lc code=end
