'''
PREFIX

Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
 NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
'''

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        root = {}
        root_type = type(root)
        for word in A:
            walk = root
            for i, ch in enumerate(word):
                if ch in walk:
                    if type(walk[ch]) == root_type:
                        walk = walk[ch]
                    else:
                        other = walk[ch]
                        walk[ch] = {other[i+1]:other}
                        walk = walk[ch]
                else:
                    walk[ch] = word
                    break
        out = []
        for word in A:
            walk = root
            for i, ch in enumerate(word):
                if type(walk[ch]) != root_type:
                    out.append(word[:i+1])
                    break
                else:
                    walk = walk[ch]
        return out
                
                    
