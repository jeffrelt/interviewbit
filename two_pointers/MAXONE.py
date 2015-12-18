'''
MAXONE
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.

Example:

Input : 
Array = {1 1 0 1 1 0 0 1 1 1 } 
M = 1

Output : 
[0, 1, 2, 3, 4] 

If there are multiple possible solutions, return the sequence which has the minimum start index.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        l = h = 0
        best = bl = bh = 0
        count = 0
        while h < len(A):
            if A[h] == 0:
                count +=1
            while count > B:
                if A[l] == 0:
                    count-=1
                l+=1
            h+=1
            score = h-l
            if best < score:
                best,bl,bh = score,l,h
        return range(bl,bh)
