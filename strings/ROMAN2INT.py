'''
ROMAN2INT
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at Roman Numeric System

Example :

Input : "XIV"
Return : 14
Input : "XX"
Output : 20
'''

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        last = None
        tot = 0
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for r in A:
            val = d[r]
            tot+=val
            if last and last < val:
                val-=(last+last)
            if r in 'IXC':
                last = val
            else:
                last = None
        return tot
