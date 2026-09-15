class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        darr={}
        sum1=[]
        for i in arr:
            if i not in darr.keys():
                darr[i]=1
            else:
                darr[i]+=1
        for i in darr.values():
            sum1.append(i)
        if(len(set(sum1))==len(sum1)):
            return True
        else:
            return False
