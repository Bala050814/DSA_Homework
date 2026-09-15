class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        darr={}
        sum1=0
        for i in nums:
            if i not in darr.keys():
                darr[i]=1
            else:
                darr[i]+=1
        for i in darr.keys():
            if darr[i]==1:
                sum1+=i
        return sum1

        
