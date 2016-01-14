'''
SUBSTRING
You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
'''

base = 9

class rollhash:
    def __init__(self):
        self.h = 0
        self.c = 0
        
    def add(self, ch):
        self.h*=base
        self.h+=ord(ch)
        self.c+=1
        
    def val(self):
        return self.h
        
    def count(self):
        return self.c
        
    def reset(self):
        self.h = 0
        self.c = 0

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        d = {}
        out = []
        rh = rollhash()
        longest = 0
        total = -1
        for word in B:
            rh.reset()
            for ch in word:
                rh.add(ch)
            if rh.val() in d:
                d[rh.val()][0]+=1
            else:
                d[rh.val()]=[1,word]
            longest = max(rh.count(), longest)
            total+=rh.count()
        i = 0
        rh.reset()
        dset = {key:d[key][0] for key in d}
        count = -1
        while i < len(A):
            rh.add(A[i])
            count+=1
            if rh.val() in dset and d[rh.val()][1] == A[i-rh.count()+1:i+1]:
                dset[rh.val()]-=1
                if dset[rh.val()] == 0:
                    del dset[rh.val()]
                rh.reset()
                if not dset:
                    out.append(i-count)
                    i-=count
                    rh.reset()
                    dset = {key:d[key][0] for key in d}
                    count = -1
                
            elif rh.count() > longest:
                i-=count
                rh.reset()
                dset = {key:d[key][0] for key in d}
                count = -1
            i+=1
        return out
