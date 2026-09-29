class Solution:

	
	def removeDuplicates(self, s):
	    # code here
	    ns="".join(dict.fromkeys(s))
	    return ns
