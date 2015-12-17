'''
REMDUP
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]. 
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        al = len(A)
        i = 1
        last = A[0]
        c = 0
        while i < al:
            if A[i] == last:
                c+=1
            elif c:
                A[i-c]=A[i]
            last = A[i]
            i+=1
        while c:
            A.pop()
            c-=1
        return len(A)
