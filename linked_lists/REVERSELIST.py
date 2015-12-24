'''
REVERSELIST
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question. 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        count = 1
        walk = ListNode(0)
        walk.next = A
        A = walk
        while walk.next:
            if count >= m:
                if count == m:
                    base = walk
                    walk = walk.next
                elif count <= n:
                    move_this = walk.next
                    hold_pri = base.next
                    hold_rest = move_this.next
                    base.next = move_this
                    move_this.next = hold_pri
                    walk.next = hold_rest
                else:
                    break
            else:
                walk = walk.next
            count+=1
        return A.next
