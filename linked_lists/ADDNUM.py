'''
ADDNUM
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        ovf=0
        walk = anchor = ListNode(0)
        while 1:
            if A:
                if B:
                    val = A.val+B.val+ovf
                    B = B.next
                else:
                    val=A.val+ovf
                A = A.next
            elif B:
                val=B.val+ovf
                B = B.next
            else:
                if ovf:
                    val=1
                else:
                    break
            if val >= 10:
                val-=10
                ovf = 1
            else:
                ovf = 0
            walk.next = ListNode(val)
            walk=walk.next
            
        return anchor.next
