"""

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

"""

import functools
class Solution:
    
    def cmp(self,a,b):
        s1=str(a)
        s2=str(b)
        num1=int(s1+s2)
        num2=int(s2+s1)
        if(num1<num2):
            return 1
        else:
            return -1
        

    def largestNumber(self, A):
        A=sorted(A,key=functools.cmp_to_key(self.cmp))
        ans=""
        for c in A:
            ans+=str(c)
        
        return int(ans)
            
