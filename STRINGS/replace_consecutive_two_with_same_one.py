class Solution:
    def removeDuplicates(self, s):
        # code here
        from itertools import groupby
        ns="".join(i for i,_ in groupby(s))
        return ns
