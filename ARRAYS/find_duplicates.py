class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        darr={}
        lis=[]
        for i in nums:
            if i not in darr.keys():
                darr[i]=1
            else:
                darr[i]+=1
        for i in darr.keys():
            if darr[i]==2:
                lis.append(i)
        
        return lis
