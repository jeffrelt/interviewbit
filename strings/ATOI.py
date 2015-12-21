'''
ATOI
Please Note:

There are certain questions where the interviewer would intentionally frame the question vague.
The expectation is that you will ask the correct set of clarifications or state your assumptions before you jump into coding.

Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.

 Questions: Q1. Does string contain whitespace characters before the number?
A. Yes Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise. 
Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
If you do, we will disqualify your submission retroactively and give you penalty points.
'''

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        nums=[]
        zero = ord('0')
        started = False
        neg = False
        for x in A:
            val = ord(x)-zero
            if val >= 0 and val <= 9:
                nums.append(val)
                started = True
            elif started:
                break
            elif x == '-':
                neg = True
                started = True
            elif x == '+':
                started = True
            elif x != ' ':
                break
        power = 1
        tot = 0
        for x in reversed(nums):
            tot+=x*power
            power*=10
        if neg:
            return -min(tot,2147483648)
        return min(tot,2147483647)
