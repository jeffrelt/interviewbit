'''
TEXTJUST
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
 Note: Each word is guaranteed not to exceed L in length. 
'''

from math import ceil

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        if len(A) < 1:
            return []
        output = []
        words = []
        remain = B
        for word in A:
            if len(words) == 0:
                l = len(word)
            else:
                l = len(word)+1
            if l <= remain:
                words.append(word)
                remain-=l
            else:
                build = ''
                if len(words) == 1:
                    build=words[0]+' '*remain
                else:
                    count = len(words)-1
                    for w in words:
                        build+=w
                        if count:
                            gap = int(ceil((remain*1.0)/count))
                            remain-=gap
                            build+=' '*(gap+1)
                        count-=1
                output.append(build)
                words=[word]
                remain=B-len(word)
        if words:
            build = ''
            if len(words) == 1:
                build=words[0]+' '*remain
            else:
                count = len(words)-1
                for w in words:
                    build+=w
                    if count:
                        build+=' '
                    count-=1
                build+=' '*remain
            output.append(build)
            words=[word]
            remain=B-len(word)
        return output
