from typing import List

class sol:
    def three_sum(self,num:List[int]) -> List[List[int]]:
        ans=[]
        num.sort()
        
        for i in range(len(num)-2):
            if i>0 and num[i]==num[i-1]:
                continue
            l = i+1
            r = len(num)-1
            while l<r:
                temp = num[i]+num[l]+num[r]
                if temp<0:
                    r-=1
                if temp>0:
                    l+=1    
                if temp==0:
                    triplet = [num[i],num[l],num[r]]
                    ans.append(triplet)
                    if l<r and num[l]==triplet[1]: ## to avoid duplicacy
                        l+=1
                    if l<r and num[r]==triplet[2]:## to avoid duplicacy
                        r-=1
        return ans                    

nums = [-1,0,1,2,-1,-4]
obj = sol()
print(obj.three_sum(nums))


