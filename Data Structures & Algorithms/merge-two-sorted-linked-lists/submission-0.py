# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(None)
        head = temp

        curr_1, curr_2 = list1, list2

        while curr_1 or curr_2:
            while curr_1 and curr_2:
                if curr_1.val > curr_2.val:
                    temp.next = curr_2
                    curr_2 = curr_2.next
                    temp = temp.next
                else:
                    temp.next = curr_1
                    curr_1 = curr_1.next
                    temp = temp.next
            while curr_1:
                    temp.next = curr_1
                    curr_1 = curr_1.next
                    temp = temp.next
            while curr_2:
                    temp.next = curr_2
                    curr_2 = curr_2.next
                    temp = temp.next

        return head.next