from typing import List
class Sol:
    def merge_sorted_array(self,num1:List[int],m:int,num2:List[int],n:int):
        while n>0:
            if num1[m-1] > num2[n-1] and m>0:
                num1[m+n-1] = num1[m-1]
                m-=1
            else:
                num1[m+n-1] = num2[n-1]
                n-=1   

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj = Sol()
print(nums1)
obj.merge_sorted_array(nums1,m,nums2,n)
print(nums1)