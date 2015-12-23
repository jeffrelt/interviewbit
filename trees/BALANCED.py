'''
BALANCED

Given a binary tree, determine if it is height-balanced.

 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 
          1
         / \
        2   3

Return : True or 1 

Input 2 : 
         3
        /
       2
      /
     1

Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        val_stack = []
        parent_stack = []
        type = 0
        while 1:
            if type == 0: #node to explore
                if A.left:
                    parent_stack.append((A,1)) 
                    A = A.left
                    continue
                elif A.right:
                    val_stack.append(0)
                    parent_stack.append((A,2))
                    A = A.right
                    continue
                else:
                    val_stack.append(1)
            elif type == 1: # return to parent from left
                if A.right:
                    parent_stack.append((A,2))
                    A = A.right
                    type = 0
                    continue
                else:
                    if val_stack[-1] > 1:
                        return 0
                    val_stack[-1]+=1
            else: #type == 2 :return to parent from right
                right = val_stack.pop()
                left = val_stack.pop()
                if abs(left - right) > 1:
                    return 0
                val_stack.append(max(left,right)+1)
            if parent_stack:
                A, type = parent_stack.pop()
            else:
                break
        return 1    
