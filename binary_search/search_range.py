'''
'''
SEARCHRANGE

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].

'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        alb = -1
        lb = 0
        aub = ub = len(A)-1
        while lb<=ub:
            mid = (lb+ub)>>1
            if A[mid] == B and (mid-1<0 or A[mid-1] < B):
                alb = mid
                break
            if A[mid] >= B:
                ub = mid-1
            else:
                lb = mid+1
        if alb == -1:
            return (-1,-1)
            
        lb = alb
        ub = len(A)-1
        while lb<=ub:
            mid = (lb+ub)>>1
            if A[mid] == B and (mid+1>=len(A) or A[mid+1] > B):
                aub = mid
                break
            if A[mid] <= B:
                lb = mid+1
            else:
                ub = mid-1
                
        
        return [alb,aub]
        
        
