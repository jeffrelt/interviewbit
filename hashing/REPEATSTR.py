'''
REPEATSTR
Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        d = {}
        best = 0
        for i in xrange(len(A)):
            if A[i] not in d:
                d[A[i]] = i
            else:
                best = max(best,len(d))
                old_i = d[A[i]]
                d[A[i]] = i
                for p in tuple(d):
                    if d[p] < old_i:
                        del d[p]
                
        return max(best,len(d))
