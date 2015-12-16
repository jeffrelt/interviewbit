'''
3SUM
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A = sorted(A)
        lb = 0
        i = 1
        j = ub = len(A)-1
        target = B-(A[lb]+A[i])
        best = A[j]-target
        while ub - lb >=2:
            val = A[j]
            if val == target:
                return B
            if abs(best) > abs(val-target):
                best = val-target
                
            if i+1 == j:
                lb+=1
                i=lb+1
                j = ub
                target = B-(A[lb]+A[i])
            elif val < target:
                i+=1
                target = B-(A[lb]+A[i])
            elif lb+1 == i:
                j-=1
                ub=j
            else:
                j-=1
                
        return B+best
        
