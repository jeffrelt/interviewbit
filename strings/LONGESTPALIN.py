'''
LONGESTPALIN
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
'''
def pal(A,c):
    '''returns bounds of the pal, c is the center'''
    
    if c+1 < len(A) and A[c] == A[c+1]:
        go = [(c-1,c+2),(c-1,c+1)]
    else:
        go = [(c-1,c+1)]
    best = (0,0)
    
    while go:
        lb,ub = go.pop()
        while lb>=0 and ub<len(A):
            if A[lb] != A[ub]:
                break
            lb-=1
            ub+=1
        ans = (lb+1,ub)
        if ans[1]-ans[0]>best[1]-best[0]:
            best=ans
    return best
    

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        lb=ub=0
        for i in xrange(len(A)):
            l,u = pal(A,i)
            if u-l > ub-lb:
                lb,ub=l,u
        return A[lb:ub]
        
